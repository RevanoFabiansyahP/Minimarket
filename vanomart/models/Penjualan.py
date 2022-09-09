from email.policy import default
from logging import exception
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Penjualan(models.Model):
    _name = 'vanomart.penjualan'
    _description = 'New Description'

    name = fields.Char(string='No Nota')
    nama_pembeli = fields.Char(string='Nama Pembeli')
    tgl_penjualan = fields.Datetime(string='Tanggal Transaksi', 
                                    default = fields.Datetime.now())
    total_bayar = fields.Integer(compute='_compute_totalbayar', string='Total Pembayaran')
    detailpenjualan_ids = fields.One2many(comodel_name='vanomart.detailpenjualan', 
                                          inverse_name='penjualan_id', 
                                          string='Detail Penjualan')
    @api.depends('detailpenjualan_ids')
    def _compute_totalbayar(self):
        for rec in self:
            a = sum(self.env['vanomart.detailpenjualan'].search([('penjualan_id', '=', rec.id)]).mapped('subtotal'))
            rec.total_bayar = a

    @api.ondelete(at_uninstall=False)
    def _ondelete_penjualan(self):
        if self.detailpenjualan_ids:
            a=[]
            for rec in self:
                a = self.env['vanomart.detailpenjualan'].search([('penjualan_id','=',rec.id)])
                print(a)
            for ob in a:
                print(str(ob.barang_id.name) + ' ' + str(ob.qty))
                ob.barang_id.stok += ob.qty
        

    # Untuk Odoo 14
    # def unlink(self):
    #     if self.detailpenjualan_ids:
    #         a=[]
    #         for rec in self:
    #             a = self.env['vanomart.detailpenjualan'].search([('penjualan_id','=',rec.id)])
    #             print(a)
    #         for ob in a:
    #             print(str(ob.barang_id.name) + ' ' + str(ob.qty))
    #             ob.barang_id.stok += ob.qty
    #     record = super (Penjualan,self).unlink()
    
    def write (self,vals):
        for rec in self:
            a = self.env['vanomart.detailpenjualan'].search([('penjualan_id','=',rec.id)])
            print(a)
            for data in a:
                print(str(data.barang_id.name)+' '+str(data.qty)+' '+str(data.barang_id.stok))
                data.barang_id.stok += data.qty
        record = super (Penjualan,self).write(vals)
        for rec in self:
            b = self.env['vanomart.detailpenjualan'].search([('penjualan_id','=',rec.id)])
            print(a)
            print(b)
            for databaru in b:
                if databaru in a:
                    print(str(databaru.barang_id.name)+' '+str(databaru.qty)+' '+str(databaru.barang_id.stok))
                    databaru.barang_id.stok -= databaru.qty
                else:
                    pass
        return record

    _sql_constraints = [
        ('no_nota_unik','unique (name)','Nomor Nota Tidak Boleh Sama !')
    ]
    
class DetailPenjualan(models.Model):
    _name = 'vanomart.detailpenjualan'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    penjualan_id = fields.Many2one(comodel_name='vanomart.penjualan', 
                                   string='Detail Penjualan',)
    barang_id = fields.Many2one(comodel_name='vanomart.barang', 
                                   string='List Barang')
    harga_satuan = fields.Integer(string='Harga Satuan')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')
    
    @api.depends('harga_satuan', 'qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.qty * rec.harga_satuan
    
    @api.onchange('barang_id')
    def onchange_barang_id(self):
        if (self.barang_id.harga_jual):
            self.harga_satuan = self.barang_id.harga_jual

    @api.model
    def create(self, vals):
        record = super(DetailPenjualan,self).create(vals)
        if record.qty:
            self.env['vanomart.barang'].search([('id','=', record.barang_id.id)]).write({'stok': record.barang_id.stok - record.qty})
        return record

    @api.constrains('qty')
    def check_quantity(self):
        for rec in self:
            if rec.qty <1:
                raise ValidationError("Mau belanja {} Berapa Banyak Sih Ka :)".format(rec.barang_id.name))
            elif (rec.barang_id.stok < rec.qty):
                raise ValidationError("Maaf Stok {} tidak mencukupi, hanya tersedia {}".format(rec.barang_id.name,rec.barang_id.stok))
from odoo import api, fields, models

class KelompokBarang(models.Model):
     _name = 'vanomart.kelompokbarang'
     _description = 'New Description'

     name = fields.Selection([
        ('makananbasah', 'Makanan Basah'), ('makanankering', 'Makanan Kering'), ('minuman','Minuman')
    ], string='Nama Kelompok')
    
     kode_kelompok = fields.Char(onchange='_compute_field_name', string='Kode Kelompok')
    
     @api.onchange('name')
     def _compute_kode_kelompok(self):
        if (self.name=='makananbasah'):
            self.kode_kelompok = 'mak01'
        elif (self.name == 'makanankering'):
            self.kode_kelompok = 'mak02'
        elif (self.name == 'minuman'):
            self.kode_kelompok = 'min01'       

     kode_kelompok = fields.Char(string='Kode Kelompok')
     kode_rak = fields.Char(string='Kode Rak')
     barang_ids = fields.One2many(comodel_name='vanomart.barang', 
                                  inverse_name='kelompokbarang_id', 
                                  string='Daftar Barang')
     jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah Item')
    
     @api.depends('barang_ids')
     def _compute_jml_item(self):
        for rec in self:
            a = self.env['vanomart.barang'].search([('kelompokbarang_id','=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_item = b
            rec.daftar = a

     daftar = fields.Char(string='Daftar Isi')
from odoo import api, fields, models

class BarangDatang(models.TransientModel):
    _name = 'vanomart.barangdatang'
     
    
    barang_id = fields.Many2one(
        comodel_name='vanomart.barang',
        string='Nama Barang',
        required=True)

    jumlah = fields.Integer(
        string='Jumlah',
        required=False)

    def button_barang_datang(self):
        for rec in self:
            self.env['vanomart.barang'].search([('id', '=', rec.barang_id.id)]).write({'stok':rec.barang_id.stok + rec.jumlah})
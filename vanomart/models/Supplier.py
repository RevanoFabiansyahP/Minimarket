from odoo import api, fields, models


class Supp(models.Model):
    _name = 'vanomart.supplier'
    _description = 'New Description'

    name = fields.Char(string='Nama Perushaan')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telepon')
    barang_id = fields.Many2many(comodel_name='vanomart.barang', string='Barang')
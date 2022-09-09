from odoo import api, fields, models


class Person(models.Model):
    _name = 'vanomart.person'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Datetime(string='Tanggal Lahir')


class Kasir(models.Model):
    _name = 'vanomart.kasir'
    _inherit = 'vanomart.person'
    _description = 'New Description'

    id_kasir = fields.Char(string='ID Kasir')


class CleaningService(models.Model):
    _name = 'vanomart.cleaningservice'
    _inherit = 'vanomart.person'
    _description = 'New Description'
    id_cln = fields.Char(string='ID Cleaning Service')
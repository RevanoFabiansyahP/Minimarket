from odoo import api, fields, models

class Konsumen(models.Model):
    _inherit = 'res.partner'
    _description = 'konsumen'

    poin = fields.Integer(string='Poin')
    level = fields.Integer(string='Level')
    
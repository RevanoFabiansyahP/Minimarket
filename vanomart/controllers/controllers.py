from odoo import http, models, fields
from odoo.http import request
import json

class Vanomart(http.Controller):
    @http.route('/vanomart/getbarang', auth='public', method=['GET'])
    def getBarang(self, **kw):
        barang = request.env['vanomart.barang'].search([])
        isi = []
        for bb in barang:
            isi.append({
                'nama_barang' :bb.name,
                'harga_jual' : bb.harga_jual,
                'stok': bb.stok
            })
        return json.dumps(isi)

class Vanomart(http.Controller):
    @http.route('/vanomart/getsupplier', auth='public', method=['GET'])
    def getSupplier(self, **kw):
        supplier = request.env['vanomart.supplier'].search([])
        sup = []
        for s in supplier:
            sup.append({
                'nama_perusahaan' : s.name,
                'alamat' : s.alamat,
                'no_telpon' : s.no_telp,
                'nama_barang' : s.barang_id[0].name
            })
        return json.dumps(sup)

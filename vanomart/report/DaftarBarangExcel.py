from turtle import width
from odoo import models, fields

class ReportBarang(models.AbstractModel):
    _name = 'report.vanomart.report_barang_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()
    
    def generate_xlsx_report(self, workbook, data, barang):
        sheet = workbook.add_worksheet('Daftar Barang')
        bold = workbook.add_format({'bold': True})
        
        sheet.write(0, 0, 'Tanggal Laporan :', bold)
        sheet.write(0, 1, str(self.tgl_lap))
        sheet.write(2, 0, 'Nama Barang', bold)
        sheet.write(2, 1, 'Harga Modal', bold)
        sheet.write(2, 2, 'Harga Jual', bold)
        sheet.write(2, 3, 'Stok', bold)
        sheet.write(2, 4, 'Kelompok Barang', bold)
        sheet.write(2, 5, 'Supplier Penerima', bold)

        row = 3
        col = 0
        for obj in barang:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.harga_beli)
            sheet.write(row, col+2, obj.harga_jual)
            sheet.write(row, col+3, obj.stok)
            for xxx in obj.kelompokbarang_id:
                sheet.write(row, col +4, xxx.name)
            for xxx in obj.supplier_id:
                sheet.write(row, col +5, xxx.name)
                col += 1
            row += 1
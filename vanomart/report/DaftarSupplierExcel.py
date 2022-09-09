from odoo import models, fields

class ReportSupplier(models.AbstractModel):
    _name = 'report.vanomart.report_supplier_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()
    
    def generate_xlsx_report(self, workbook, data, supplier):
        sheet = workbook.add_worksheet('Daftar Supplier')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, 'Tanggal Laporan :', bold)
        sheet.write(0, 1, str(self.tgl_lap))
        sheet.write(2, 0, 'Nama Perusahaan', bold)
        sheet.write(2, 1, 'Alamat', bold)
        sheet.write(2, 2, 'No Telepon', bold)
        sheet.write(2, 3, 'Produk & Barang', bold)

        row = 3
        col = 0
        for obj in supplier:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.alamat)
            sheet.write(row, col+2, obj.no_telp)
            for xxx in obj.barang_id:
                sheet.write(row, col +3, xxx.name)
                col += 1
            row += 1
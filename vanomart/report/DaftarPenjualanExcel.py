from datetime import timedelta
from odoo import models, fields

class ReportPenjualan(models.AbstractModel):
    _name = 'report.vanomart.report_penjualan_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()
    
    def generate_xlsx_report(self, workbook, data, penjualan):
        sheet = workbook.add_worksheet('Riwayat Penjualan')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, 'Tanggal Laporan :', bold)
        sheet.write(0, 1, str(self.tgl_lap))
        sheet.write(2, 0, 'No Nota', bold)
        sheet.write(2, 1, 'Nama Pembeli', bold)
        sheet.write(2, 2, 'Tanggal Transaksi', bold)
        sheet.write(2, 3, 'Nama Barang', bold)
        sheet.write(2, 4, 'Harga', bold)
        sheet.write(2, 5, 'Jumlah Beli', bold)
        sheet.write(2, 6, 'Subtotal', bold)
        sheet.write(2, 7, 'Total Pembayaran', bold)

        row = 3
        col = 0
        for obj in penjualan:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.nama_pembeli)
            sheet.write(row, col+2, (obj.tgl_penjualan+ timedelta(hours=7)).strftime("%d/%m/%Y, %H:%M:%S"))
            sheet.write(row, col+7, obj.total_bayar)
            for xxx in obj.detailpenjualan_ids:
                sheet.write(row, col +3, xxx.barang_id.name)
                sheet.write(row, col +4, xxx.harga_satuan)
                sheet.write(row, col +5, xxx.qty)
                sheet.write(row, col +6, xxx.subtotal)
                row += 1
            row += 1
# -*- coding: utf-8 -*-
{
    'name': "vanomart",

    'summary': """
        welcome to my project""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',
    'application': True,


    # any module necessary for this one to work correctly
    'depends': ['base','report_xlsx',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/menu.xml',
        'views/kelompokbarang_view.xml',
        'views/barang_view.xml',
        'views/person_view.xml',
        'views/kasir_view.xml',
        'views/cleaning_view.xml',
        'views/konsumen_view.xml',
        'views/direksi_view.xml',
        'views/supplier_view.xml',
        'views/penjualan_view.xml',
        'report/report.xml',
        'report/reportpenjualanpdf.xml',
        'wizzard/barangdatang_wizzard_view.xml',
 
    ],
    #  only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
      
    # ],
}
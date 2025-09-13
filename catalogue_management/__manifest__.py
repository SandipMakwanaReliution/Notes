# -*- coding: utf-8 -*-
{
    'name': "Catalogue Management",
    'summary': """
        Catalogue Management.
    """,
    'description': """
    """,
    'author': "Reliution",
    'website': "",
    'license': 'OPL-1',
    'version': '17.0.0.1',
    'category': '',
    'depends': ['base', 'sale', 'sale_stock', 'res_area', 'product_customization'],
    'data': [
        'security/ir.model.access.csv',
        'security/data.xml',
        'data/ir_cron.xml',
        'views/catalogue_management.xml',
        'views/product_view.xml',
        'views/res_partner_views.xml',
        'views/sale_order_line_view.xml',
        'views/catalogue_management_line.xml',
        'views/catalogue_info.xml',
        'report/report_catalogue.xml',
        'report/report_catalogue_template.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': 0
}

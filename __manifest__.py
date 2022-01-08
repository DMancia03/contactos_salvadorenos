# -*- coding: utf-8 -*-
{
    'name': "Contactos Salvadoreños | Diego Mancía",

    'summary': """
        Modulo que permite implementar campos específicos de El Salvador a los contactos.""",

    'description': """
        Modulo creado para poder registrar los contactos con más detalles acerca de las leyes salvadoreñas y crear sucursales por compañía.
    """,

    'author': "Diego Mancía",
    'website': "http://www.treming.com",
    'category': 'Sales',
    'version': '0.1',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/contact_views.xml',
        'views/sucursal_views.xml',
        'views/sale_order_views.xml'
    ]
}

# -*- coding: utf-8 -*-

{
    'name': 'Library management',

    'summary': 'Library management, Academy app to manage Training',

    'description': """
        Library management
    """,

    'author': 'Itnnovation',
    
    'website': '',
    
    'category': 'Training',
    
    'version': '16.0',
    
    'depends': ['base'],
    
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menuitems.xml',
        'views/library_book_views.xml',
        'views/library_book_copy_views.xml',
        'views/library_rental_views.xml',
    ],

    'demo': [
        'demo/demo_book_data.xml',
    ],
    
    'license': 'Other proprietary',
}
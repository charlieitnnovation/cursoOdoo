# -*- coding: utf-8 -*-

from odoo import http

class Libray(http.Controller):
    @http.route('/library/', auth='public', website=True)
    def index(self, **kw):
        return 'Test website'

    @http.route('/library/libros_disponibles/', auth='public', website=True)
    def libros_disponibles(self, **kw):
        libros_rentados_list = []
        libros_inventario_list = []
        
        libros_rentados = http.request.env['library.rental.line'].search([
                ('returned', '=', 'false'),
            ])
        for libro in libros_rentados:
            libros_rentados_list.append({
                    'libro': libro.book_copy_id.book_id.name,
                    'referencia': libro.book_copy_id.internal_reference,
                })
            
        libros_inventario = http.request.env['library.book.copy'].search([])
        for libro in libros_inventario:
            libros_inventario_list.append({
                    'libro': libro.book_id.name,
                    'referencia': libro.internal_reference,
                })

        print(':::::::::::::::::: %s'%libros_rentados_list)
        print(':::::::::::::::::: %s'%libros_inventario_list)

        libros_disponibles = [libro for libro in libros_inventario_list if libro not in libros_rentados_list]
        
        return http.request.render('library_management.library_website', {
            'libros_disponibles': libros_disponibles,
        })
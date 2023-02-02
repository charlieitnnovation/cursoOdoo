# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibrayRentalReportWizard(models.TransientModel):

    _name = 'library.rental.report.wizard'
    _description = 'Reporte de renta de libros'
    
    book_id = fields.Many2one(
        string = 'Libro',
        comodel_name = 'library.book',
        required = True,
    )
    partner_id = fields.Many2one(
        string = 'Cliente',
        comodel_name = 'res.partner',
        required = True,
    )

    def open_rental_report(self):
        
        list_books = []
        library_rental = self.env['library.rental'].search([
            ('partner_id', '=', self.partner_id.id)
        ])
    
        for rental in library_rental:
            for book_copy in rental.book_ids:
                if book_copy.book_copy_id.book_id == self.book_id:
                    list_books.append({
                        'book': book_copy.book_copy_id.name,
                        'reference': book_copy.book_copy_id.internal_reference,
                    })
         
        data = {
            'form': self.read()[0],
            'list_books': list_books,
        }
        
        print(self.read()[0])
        
        return self.env.ref('library_management.action_report_library_list_books').report_action(self, data=data)
        
        #result = ','.join(["%s%s"%(item['book'], item['reference']) for item in list_books])
        #raise ValidationError(result)
        
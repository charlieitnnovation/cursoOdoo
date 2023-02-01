# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class LibraryRental(models.Model):
    
    _name = 'library.rental'
    _description = 'Customer rental information'
    
    partner_id = fields.Many2one(
        string = 'Cliente',
        comodel_name = 'res.partner',
    )
    date = fields.Date(
        string = 'Fecha de renta',
        default = datetime.now(),
    )
    book_ids = fields.One2many(
        string = 'Libros rentados',
        comodel_name = 'library.rental.line',
        inverse_name = 'rental_id',
    )

    def name_get(self):
        result = []
        for record in self:
            if record.exists():
                result.append((record.id, 'Renta %s'%record.id))
            else:
                result.append((record.id, 'Nueva renta'))

        return result

    
class LibraryRentalLine(models.Model):
    
    _name = 'library.rental.line'
    _description = 'Customer rental of book information'
    
    rental_id = fields.Many2one(
        string = 'Renta de cliente',
        comodel_name = 'library.rental',
    )
    book_id = fields.Many2one(
        string = 'Libro',
        comodel_name = 'library.book',
    )
    book_copy_id = fields.Many2one(
        string = 'Libro',
        comodel_name = 'library.book.copy',
    )
    returned = fields.Boolean(
        string = 'Regresado',
        default = False,
    )
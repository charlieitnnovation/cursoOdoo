# -*- coding: utf-8 -*-

from odoo import models, fields

class LibrayBookCopy(models.Model):
    
    _name = 'library.book.copy'
    _description = 'Book specific copy information'
    _inherits = {'library.book': 'book_id'}
    
    book_id = fields.Many2one(
        string = 'Libro',
        comodel_name = 'library.book',
        required = True,
        ondelete = "cascade",
    )
    internal_reference = fields.Char(
        string = 'Referencia interna',
    )
    
    def name_get(self):
        result = []
        for record in self:
            if record.exists():
                result.append((record.id, '%s %s'%(record.name, record.internal_reference)))
            else:
                result.append((record.id, 'Nuevo libro'))

        return result

# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Book(models.Model):
    
    _name = 'library.book'
    _description = 'Book information'
    
    name = fields.Char(
        string = 'Name',
    )
    authors = fields.Char(
        string = 'Authors',
    )
    editors = fields.Char(
        string = 'Editors',
    )
    publisher = fields.Char(
        string = 'Publisher',
    )
    edition_year = fields.Integer(
        string = 'Edition year',
    )
    isbn = fields.Char(
        string = 'ISBN',
    )
    genre = fields.Selection(
        string = 'Genre',
        selection = [
            ('Novela', 'Novela'),
            ('Cuento', 'Cuento'),
            ('Leyenda', 'Leyenda'),
            ('Mito', 'Mito'),
            ('Fábula', 'Fábula'),
            ('Cantar de gesta', 'Cantar de gesta'),
            ('Relato', 'Relato'),
            ('Epopeya', 'Epopeya'),
            ('Lírico', 'lírico'),
            ('Canción', 'Canción'),
            ('Himno', 'Himno'),
            ('Soneto', 'Soneto'),
            ('Oda', 'Oda'),
            ('Villancico', 'Villancico'),
            ('Pastorela', 'Pastorela'),
            ('Letrilla', 'Letrilla'),
            ('Madrigal', 'Madrigal'),
            ('Elegía', 'Elegía'),
            ('Égloga', 'Égloga'),
            ('Sátira', 'Sátira'),
            ('Dramático', 'Dramático'),
            ('Musical', 'Musical'),
            ('Biografía', 'Biografía'),
            ('Consulta', 'Consulta'),
        ],
    )
    active = fields.Boolean(
        string = "Activo",
    )
    note = fields.Text(
        string = "Nota",
    )

    @api.onchange('isbn')
    def onchange_isbn(self):
        if self.isbn and len(self.isbn) != 13:
            return {
                'warning': {'title': "Error de validación", 'message': "El campo ISBN debe tener 13 caracteres", 'type': 'notification'},
                'value': {'isbn': self._origin.isbn}
            }
        
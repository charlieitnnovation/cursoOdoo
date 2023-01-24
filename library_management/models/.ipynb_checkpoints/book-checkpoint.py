# -*- coding: utf-8 -*-

from odoo import models, fields, api

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
        string = 'ISN',
    )
    genre = fields.Char(
        string = 'Genre',
    )

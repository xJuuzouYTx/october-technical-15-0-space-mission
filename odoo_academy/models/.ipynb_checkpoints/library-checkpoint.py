#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Book(models.Model):
    _name = 'odoo_academy.book'
    _description = 'Libro'
    
    nombre = fields.Char(string="Nombre")
    genero = fields.Selection(string="Genero", selection=[('terror', 'Terror'),
                                                         ('drama', 'Drama'),
                                                         ('fantasia', 'Fantasia')])
    editorial = fields.Many2one('odoo_academy.editorial')
    ano_edicion = fields.Integer(string="Año de edición")
    isbn = fields.Char(string="ISBN")
    
    
class Editorial(models.Model):
    _name = 'odoo_academy.editorial'
    _descripcion = 'Editorial info'
    
    nombre = fields.Char(string="Nombre de la editorial")
    
    
    
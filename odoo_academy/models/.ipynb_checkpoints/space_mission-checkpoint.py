#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Ship(models.Model):
    _name = 'odoo_academy.ship'
    _description = 'Nave espacial'
    
    dimensiones = fields.Integer(string='Dimensiones del barco')
    tipo_combustible = fields.Selection(string='Tipo de combustible',selection=[('gasolina','Gasolina')]
    tipo_barco = fields.Selection(string='Tipo de barco', selection=[('barco','Barco'),
                                                                     ('nave','Nave'),
                                                                     ('auto','Automovil')])
    num_pasajeros = fields.Integer(string='Número de pasajeros')
    active = fields.Boolean(string='Active', default=True)
    
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

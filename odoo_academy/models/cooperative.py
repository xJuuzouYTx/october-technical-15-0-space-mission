#-*- coding: utf-8 -*-

from odoo import models, fields

class Tarea(models.Model):
    _name = 'odoo_academy.task'
    
    hora_inicio = fields.Datetime(string="Hora de incio")
    hora_fin = fields.Datetime(string="Hora de fin")
    
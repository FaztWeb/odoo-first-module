# -*- coding: utf-8 -*-
from odoo import models, fields

class Student(models.Model):
    _name = "school.student"  
    _description = "Tabla de Estudiantes"

    name = fields.Char(string="Nombre", required=True)
    age = fields.Integer(string="Edad")
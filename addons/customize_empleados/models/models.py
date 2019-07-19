# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = "res.partner"
    ruc = fields.Char("RUC")
    fecha_cumple = fields.Date("Fecha de cumpleaños")
    tipo = fields.Selection(selection=[("tipo1","Tipo 1"),("tipo2","Tipo 2")])

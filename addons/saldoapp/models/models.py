# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Movimiento(models.Model):
    _name = "sa.movimiento" # Nombre de la tabla en la BD = sa_movimiento
    _description = "Movimientos" # Descripción para Odoo 
    _rec_name = "descripcion"

    #Definir los campos de la tabla
    descripcion = fields.Char(string="Descripción",required=True)
    fecha = fields.Date(string="Fecha")
    monto = fields.Float(string="Monto")
    numero_comprobante = fields.Char(string="Número de Comprobante")
    foto_comprobante = fields.Binary(string="Foto de Comprobante")

    tipo = fields.Selection(string="Tipo",selection=[("ingreso","Ingreso"),("egreso","Egreso")])
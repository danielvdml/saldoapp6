# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Movimiento(models.Model):
    _name = "sa.movimiento" # Nombre de la tabla en la BD = sa_movimiento
    _description = "Movimientos" # Descripción para Odoo 
    _rec_name = "descripcion"

    #Definir los campos de la tabla
    descripcion = fields.Char(string="Descripción",required=True)
    fecha = fields.Date(string="Fecha")

    def _default_monetary(self):
        usuario_id = self.env.uid
        usuario_obj = self.env["res.users"].search([("id","=",usuario_id)])
        if usuario_obj:
            partner_id = usuario_obj.partner_id
            currency_id = partner_id.currency_id.id
            return currency_id
            #company_id = usuario_obj.company_id
            #currency_id = company_id.currency_id.id
            #return currency_id
        else:
            return False

    currency_id = fields.Many2one("res.currency",string="Moneda",default=_default_monetary)

    state = fields.Selection(selection=[('borrador','Borrador'),('validado','Validado')],default="borrador")
    

    monto = fields.Monetary(string="Monto",currency="currency_id")

    numero_comprobante = fields.Char(string="Número de Comprobante")
    foto_comprobante = fields.Binary(string="Foto de Comprobante")

    tipo = fields.Selection(string="Tipo",selection=[("ingreso","Ingreso"),("egreso","Egreso")])

    usuario_id = fields.Many2one("sa.usuario",string="Usuario")
    res_user_id = fields.Many2one("res.users",string="Usuario")
    

    def validar_movimiento(self):
        for record in self:
            record.state = "validado"
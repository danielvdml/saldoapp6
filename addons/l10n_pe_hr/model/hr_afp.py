from odoo import api, fields, models, tools, _


class hr_afp(models.Model):
    _name = 'hr.afp'
    _description = 'Fondos de Pension'

    codigo = fields.Char('Codigo', required=True)
    name = fields.Char('Nombre', required=True)
    ruc = fields.Char('RUC', required=True)
    #rate = fields.Float('Tasa', required=True)
    #sis = fields.Float('Aporte Empresa', required=True)
    #independiente = fields.Float('Independientes', required=True)
    aporte = fields.Float('Aporte', required=True, default=10.0)
    seguro = fields.Float('Seguro', required=True)
    comision_flujo = fields.Float('Conmision Flujo', required=True)
    comision_mixta = fields.Float('Conmision Mixta', required=True)


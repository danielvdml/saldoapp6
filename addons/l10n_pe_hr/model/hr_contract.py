from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError
import odoo.addons.decimal_precision as dp

class hr_contract(models.Model):
    _inherit = 'hr.contract'
    _description = 'Employee Contract'

    afp_id = fields.Many2one('hr.afp', 'AFP')
    tipo_comision= fields.Selection((('mixta', 'MIXTA'), ('flujo', 'Flujo')), 'Tipo de Comisión', default="mixta")
    aporte_voluntario = fields.Float(
        'Ahorro Previsional Voluntario (APV)', help="Ahorro Previsional Voluntario (APV)")
    anticipo_sueldo = fields.Float(
        'Anticipo de Sueldo',
        help="Anticipo De Sueldo Realizado Contablemente")
    carga_familiar = fields.Float(
        'Carga Familiar Simple',
        help="Carga familiar para el cálculo de asignación familiar simple")          
    complete_name = fields.Char(related='employee_id.firstname')
    last_name = fields.Char(related='employee_id.last_name')
    gratificacion_legal = fields.Boolean('Gratificación Legal Anual')
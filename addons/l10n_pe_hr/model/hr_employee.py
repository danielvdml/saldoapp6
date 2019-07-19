import re
import logging

from odoo import models, fields, api
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    
    firstname = fields.Char("Firstname")
    last_name = fields.Char("Last Name")
    middle_name = fields.Char("Middle Name", help='Employees middle name')
    mothers_name = fields.Char("Mothers Name", help='Employees mothers name')
    type_id = fields.Many2one('hr.type.employee', 'Tipo de Empleado')

    @api.model
    def _get_computed_name(self, last_name, firstname, last_name2=None, middle_name=None):
        names = []
        if firstname:
            names.append(firstname)
        if middle_name:
            names.append(middle_name)
        if last_name:
            names.append(last_name)
        if last_name2:
            names.append(last_name2)
        return " ".join(names)

    @api.onchange('firstname', 'mothers_name', 'middle_name', 'last_name')
    def get_name(self):
        if self.firstname and self.last_name:
            self.name = self._get_computed_name(self.last_name, self.firstname, self.mothers_name, self.middle_name)

    

    

    

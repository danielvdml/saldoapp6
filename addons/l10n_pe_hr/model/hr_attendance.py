from datetime import datetime
from pytz import timezone

from odoo import models, fields, api, exceptions, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

#from odoo import models, fields, api

class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    worked_hours_extras = fields.Float(string='Worked Hours Extras', compute='_compute_worked_hours_extras', store=True, readonly=True)

    @api.depends('check_in', 'check_out', 'employee_id')
    def _compute_worked_hours_extras(self):
        for attendance in self:
            delta_in = datetime.strptime(attendance.check_in, DEFAULT_SERVER_DATETIME_FORMAT)
            delta_out = datetime.strptime(attendance.check_out, DEFAULT_SERVER_DATETIME_FORMAT)
            horas = 12.0
            if attendance.check_in:
                if len(attendance.employee_id.contract_id.working_hours.attendance_ids) > 0:
                    attendance_week = list(filter(lambda att:int(att.dayofweek) == delta_in.weekday(), attendance.employee_id.contract_id.working_hours.attendance_ids))
                        
                    if len(attendance_week) > 0 :
                        horas_antes = attendance_week[0].hour_from - ((delta_in.time().hour + delta_in.time().minute / 60.0) - 5.0)
                        horas_despues = ((delta_out.time().hour + delta_out.time().minute / 60.0) - 5.0) - attendance_week[1].hour_to

                        attendance.worked_hours_extras = horas_antes + horas_despues

                    #attendance.worked_hours_extras = attendance_week[0].hour_from - delta_in.time().replace(tzinfo=timezone('America/Lima')).hour 
                else:
                    attendance.worked_hours_extras = 0.0
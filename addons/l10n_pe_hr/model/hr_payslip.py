from pytz import timezone
from datetime import date, datetime, time

from odoo import api, fields, models, tools, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError, ValidationError


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    @api.model
    def get_worked_day_lines(self, contract_ids, date_from, date_to):
        def create_empty_worked_lines(employee_id, contract_id, date_from, date_to):
            attendance = {
                'name': 'Asistencia',
                'sequence': 5,
                'code': 'WORK100',
                'number_of_days': 0.0,
                'number_of_hours': 0.0,
                'contract_id': contract_id,
            }

            attendance25 = {
                'name': 'Horas Extras 25%',
                'sequence': 10,
                'code': 'HEXT25',
                'number_of_days': 0.0,
                'number_of_hours': 0.0,
                'contract_id': contract_id,
            }

            attendance35 = {
                'name': 'Horas Extras 35%',
                'sequence': 15,
                'code': 'HEXT35',
                'number_of_days': 0.0,
                'number_of_hours': 0.0,
                'contract_id': contract_id,
            }

            attendance_sunday = {
                'name': 'Horas Extras Domingo',
                'sequence': 20,
                'code': 'HEXTDOM',
                'number_of_days': 0.0,
                'number_of_hours': 0.0,
                'contract_id': contract_id,
            }

            valid_days = [
                ('employee_id', '=', employee_id),
                ('check_in', '>=', date_from),
                ('check_out', '<=', date_to),
            ]


            return attendance, attendance25, attendance35, attendance_sunday, valid_days

        attendances = []

        for contract in self.env['hr.contract'].browse(contract_ids):
            attendance, attendance25, attendance35, attendance_sunday, valid_days = create_empty_worked_lines(
                contract.employee_id.id,
                contract.id,
                date_from,
                date_to
            )

            for day in self.env['hr.attendance'].search(valid_days):
                #if day.worked_hours_extras > 0:
                employee = self.env['hr.contract'].employee_id;

                delta_in = datetime.strptime(day.check_in, DEFAULT_SERVER_DATETIME_FORMAT)
                delta_out = datetime.strptime(day.check_out, DEFAULT_SERVER_DATETIME_FORMAT)
                if len(contract.working_hours.attendance_ids) > 0:
                    attendance_week = list(filter(lambda att:int(att.dayofweek) == delta_in.weekday(), contract.working_hours.attendance_ids))
                        
                    if len(attendance_week) > 0 :

                        #if attendance_week[0].hour_from < 12.0 :
                        horas_antes = 8 - ((delta_in.time().hour + delta_in.time().minute / 60.0) - 5.0)
                            #horas_despues = ((delta_out.time().hour + delta_out.time().minute / 60.0) - 5.0) - attendance_week[1].hour_to
                        #else :
                            #horas_antes = attendance_week[1].hour_from - ((delta_in.time().hour + delta_in.time().minute / 60.0) - 5.0)
                        horas_despues = ((delta_out.time().hour + delta_out.time().minute / 60.0) - 5.0) - 18 #attendance_week[1].hour_to

                        if horas_antes < 1 :
                            horas_antes = 0.0

                        if horas_despues < 1 :
                            horas_despues = 0.0

                        if delta_in.weekday() == 6:
                            horas_extras = day.worked_hours
                        else:
                            horas_extras = horas_antes + horas_despues

                    #attendance.worked_hours_extras = attendance_week[0].hour_from - delta_in.time().replace(tzinfo=timezone('America/Lima')).hour 
                else:
                    horas_extras = 0.0

                if delta_in.weekday() == 6:
                    attendance_sunday['number_of_days'] += 1
                    attendance_sunday['number_of_hours'] += horas_extras-1
                else:
                    if horas_extras > 0.0:  #and horas_extras <= 2.0:
                        attendance25['number_of_days'] += 1
                        attendance25['number_of_hours'] += horas_extras
                    #else:
                     #   attendance25['number_of_days'] += 1
                      #  attendance25['number_of_hours'] += horas_extras
                       # attendance35['number_of_days'] += 1
                        #attendance35['number_of_hours'] += 0 # horas_extras - 2

            for day in self.env['hr.attendance'].search(valid_days):
                if day.worked_hours >= 0.0:
                    attendance['number_of_days'] += 1
                    attendance['number_of_hours'] += day.worked_hours

            if attendance['number_of_hours'] < 48 :
                me_falta = 48 - attendance['number_of_hours']
                if attendance25['number_of_hours'] > me_falta:
                    attendance['number_of_hours'] += attendance25['number_of_hours'] - me_falta
                    attendance25['number_of_hours'] -= attendance25['number_of_hours'] - me_falta
                else:
                    attendance['number_of_hours'] += attendance25['number_of_hours']
                    attendance25['number_of_hours'] = 0
            else:
                attendance['number_of_hours'] = 48
                attendance25['number_of_hours'] = attendance['number_of_hours'] - 48
                    #else:
                        #attendance['number_of_hours'] += 8

            # needed so that the shown hours matches any calculations you use them for
            attendance['number_of_hours'] = round(attendance['number_of_hours'], 2)
            attendances.append(attendance)           
            # needed so that the shown hours matches any calculations you use them for
            attendance25['number_of_hours'] = round(attendance25['number_of_hours'], 2)
            attendances.append(attendance25)
            attendance35['number_of_hours'] = round(attendance35['number_of_hours'], 2)
            attendances.append(attendance35)
            attendance_sunday['number_of_hours'] = round(attendance_sunday['number_of_hours'], 2)
            attendances.append(attendance_sunday)

        return super(HrPayslip, self).get_worked_day_lines(contract_ids, date_from, date_to) + attendances


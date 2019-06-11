from odoo import models,api,fields

class Usuario(models.Model):
    _name = "sa.usuario"

    _description = "Usuario"
    name = fields.Char("Nombre")
    correo = fields.Char("Correo")


class ResUsers(models.Model):
    _inherit = "res.users"
    fecha_nac = fields.Date(string = "Fecha de Nacimiento")


class ResPartner(models.Model):
    _inherit = "res.partner"
    fecha_nac = fields.Date(string = "Fecha de Nacimiento")
    currency_id = fields.Many2one("res.currency",string="Moneda por Defecto")

    def action_view_form_res_partner(self):
        usuario_id = self.env.uid
        usuario_obj = self.env["res.users"].search([("id","=",usuario_id)])
        if usuario_obj:
            partner_id = usuario_obj.partner_id
            return {
                "type":"ir.actions.act_window",
                "name":"Mi Perfil",
                "res_model":"res.partner",
                "view_id":self.env.ref("saldoapp.view_form_res_partner").id,
                "view_mode":"form",
                "res_id":partner_id.id
            }
        else:
            return False
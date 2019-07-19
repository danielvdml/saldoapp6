from odoo import api, models

class MovimientoReport(models.AbstractModel):
    _name = 'report.saldoapp.report_movimiento_consolidado'
    
    @api.model
    def _get_report_values(self, docids, data=None):
        # docids = > [5]
        partners = self.env["res.partner"].browse(docids) # Aqui tengo una list de objetos(res.partner), que va desde 1 registro a n registros
        partner_ls = []
        for partner in partners:
            #self.env["sa.movimiento"] es la tabla de sa.movimiento (ingresos y egresos)
            #self.env["sa.movimiento"].search([("create_uid","=",partner.user_id.id),('tipo','=','ingreso')]) me devuelve una lista de elementos de tipo sa.movimiento
            #filtrado por el usuario que lo creo y por el tipo de movimiento ingreso
            #ing es un objeto de sa.movimiento
            user_id = self.env["res.users"].search([("partner_id","=",partner.id)])
            if user_id.exists():
                user = user_id[0]
                ingresos = sum([ ing.monto for ing in self.env["sa.movimiento"].search([("create_uid","=",user.id),('tipo','=','ingreso')])])
                egresos = sum([ egre.monto for egre in self.env["sa.movimiento"].search([("create_uid","=",user.id),('tipo','=','egreso')])])
            else:                
                ingresos = 0
                egresos = 0
            #ingresos = sum([100,244,500])
            partner_dict = {
                "obj":partner,
                "ingresos":ingresos,
                "egresos":egresos
            }
            
            partner_ls.append(partner_dict)

        def funcionx(nombre):
            return "Un saludo para "+nombre

        docargs = {
            'partners': partner_ls,
            'parametro_1':"parametro",
            'parametro_2':"parametro",
            'parametro_3':"parametro",
            'parametro_4':"parametro",
            'funcionx':funcionx
        }
        return docargs
    """
    @api.model
    def _get_report_values(self, docids, data=None):
        # docids = > [5]
        docs = self.env["res.partner"].browse(docids)
        docargs = {
            'doc_ids': docids,
            'doc_model': "res.partner",
            'docs': docs,
            'titulo':"Programando reportes en python"
        }
        return docargs
    """
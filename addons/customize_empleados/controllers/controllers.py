# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

# class CustomizeEmpleados(http.Controller):
#     @http.route('/customize_empleados/customize_empleados/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customize_empleados/customize_empleados/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customize_empleados.listing', {
#             'root': '/customize_empleados/customize_empleados',
#             'objects': http.request.env['customize_empleados.customize_empleados'].search([]),
#         })

#     @http.route('/customize_empleados/customize_empleados/objects/<model("customize_empleados.customize_empleados"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customize_empleados.object', {
#             'object': obj
#         })


class Clientes(http.Controller):
    
    @http.route("/clientes",auth='public')
    def index(self):
        #search: devuelve resultado de busqueda como objeto
        #browse: Busqueda por Id
        #search_read: devuelve resultado de busqueda en diccionario
        clientes = request.env["res.partner"].sudo().search([])
        return http.request.render('customize_empleados.lista_clientes_otra_plantilla',{"clientes":clientes})
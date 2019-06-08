# -*- coding: utf-8 -*-
from odoo import http

# class PrepagoApp(http.Controller):
#     @http.route('/prepago_app/prepago_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prepago_app/prepago_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('prepago_app.listing', {
#             'root': '/prepago_app/prepago_app',
#             'objects': http.request.env['prepago_app.prepago_app'].search([]),
#         })

#     @http.route('/prepago_app/prepago_app/objects/<model("prepago_app.prepago_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prepago_app.object', {
#             'object': obj
#         })
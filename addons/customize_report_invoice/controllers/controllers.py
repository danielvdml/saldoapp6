# -*- coding: utf-8 -*-
from odoo import http

# class CustomizeReportInvoice(http.Controller):
#     @http.route('/customize_report_invoice/customize_report_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customize_report_invoice/customize_report_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customize_report_invoice.listing', {
#             'root': '/customize_report_invoice/customize_report_invoice',
#             'objects': http.request.env['customize_report_invoice.customize_report_invoice'].search([]),
#         })

#     @http.route('/customize_report_invoice/customize_report_invoice/objects/<model("customize_report_invoice.customize_report_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customize_report_invoice.object', {
#             'object': obj
#         })
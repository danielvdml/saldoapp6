# -*- coding: utf-8 -*-
from odoo import http

# class CustomizeReportSales(http.Controller):
#     @http.route('/customize_report_sales/customize_report_sales/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customize_report_sales/customize_report_sales/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customize_report_sales.listing', {
#             'root': '/customize_report_sales/customize_report_sales',
#             'objects': http.request.env['customize_report_sales.customize_report_sales'].search([]),
#         })

#     @http.route('/customize_report_sales/customize_report_sales/objects/<model("customize_report_sales.customize_report_sales"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customize_report_sales.object', {
#             'object': obj
#         })
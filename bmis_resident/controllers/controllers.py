# -*- coding: utf-8 -*-
# from odoo import http


# class BmisResidents(http.Controller):
#     @http.route('/bmis_residents/bmis_residents', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bmis_residents/bmis_residents/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bmis_residents.listing', {
#             'root': '/bmis_residents/bmis_residents',
#             'objects': http.request.env['bmis_residents.bmis_residents'].search([]),
#         })

#     @http.route('/bmis_residents/bmis_residents/objects/<model("bmis_residents.bmis_residents"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bmis_residents.object', {
#             'object': obj
#         })


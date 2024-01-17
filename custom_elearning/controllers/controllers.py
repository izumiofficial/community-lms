# -*- coding: utf-8 -*-
# from odoo import http


# class CustomElearning(http.Controller):
#     @http.route('/custom_elearning/custom_elearning', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_elearning/custom_elearning/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_elearning.listing', {
#             'root': '/custom_elearning/custom_elearning',
#             'objects': http.request.env['custom_elearning.custom_elearning'].search([]),
#         })

#     @http.route('/custom_elearning/custom_elearning/objects/<model("custom_elearning.custom_elearning"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_elearning.object', {
#             'object': obj
#         })


# -*- coding: utf-8 -*-
# from odoo import http


# class Space-mission(http.Controller):
#     @http.route('/space-mission/space-mission', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/space-mission/space-mission/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('space-mission.listing', {
#             'root': '/space-mission/space-mission',
#             'objects': http.request.env['space-mission.space-mission'].search([]),
#         })

#     @http.route('/space-mission/space-mission/objects/<model("space-mission.space-mission"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('space-mission.object', {
#             'object': obj
#         })

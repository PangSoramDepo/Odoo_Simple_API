# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class odoo__simple__api(models.Model):
#     _name = 'odoo__simple__api.odoo__simple__api'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
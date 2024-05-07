# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, modules,fields


class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    middle_name = fields.Char(string="Middle Name")
    company_type = fields.Selection(selection_add=[('member','Member'),('head','Head')])

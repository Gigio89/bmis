# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, modules,fields


class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    middle_name = fields.Char(string="Middle Name")
    household_type = fields.Selection(string='Household Type',
        selection=[('head','Head of the family'),('member','Member of the family')])
    #company_type = fields.Selection(selection_add=[('member','Member'),('head','Head')], compute='_compute_company_type',inverse='_write_company_type')

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, modules,fields


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    first_name = fields.Char(string="First Name",required=True)
    last_name = fields.Char(string="Last Name",required=True)
    middle_name = fields.Char(string="Middle Name")
    household_type = fields.Selection(string='Household Type',
        selection=[('head','Head of the family'),('member','Member of the family')],required=True)
    #company_type = fields.Selection(selection_add=[('member','Member'),('head','Head')], compute='_compute_company_type',inverse='_write_company_type')
    street_id = fields.Many2one(string="Street",comodel_name="bmis.street")
    barangay_id = fields.Many2one(string="Barangay",related="street_id.barangay_id")
    city_municipality_id = fields.Many2one(string="City-Municipality",related="barangay_id.city_municipality_id")
    province_id = fields.Many2one(string="Province",related="city_municipality_id.province_id")
    #region_id = fields.Many2one(string="Region",related="province_id.region_id")
    #province_id = fields.Many2one(string="Province", comodel_name="res.country.state")
    country_id = fields.Many2one(string="Country", related="province_id.country_id")

    @api.onchange("first_name","middle_name","last_name")
    def _onchange_first_name(self):
        if self.first_name and self.last_name:
            self.name = str(self.first_name) + ' ' + str(self.last_name)
            
    @api.onchange("street_id")
    def _onchange_first_name(self):
        if self.street_id:
            self.street = str(self.street_id.name)

    @api.onchange("barangay_id")
    def _onchange_first_name(self):
        if self.barangay_id:
            self.street2 = str(self.barangay_id.name)

    @api.onchange("city_municipality_id")
    def _onchange_first_name(self):
        if self.city_municipality_id:
            self.city = str(self.city_municipality_id.name)
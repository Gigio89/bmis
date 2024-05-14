# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, modules,fields
from datetime import date

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
    village_subdivision_id = fields.Many2one(string="Village/Subdibvision",related="street_id.village_subdivision_id")
    barangay_id = fields.Many2one(string="Barangay",related="street_id.barangay_id")
    city_municipality_id = fields.Many2one(string="City-Municipality",related="barangay_id.city_municipality_id")
    province_id = fields.Many2one(string="Province",related="city_municipality_id.province_id")
    country_id = fields.Many2one(string="Country", related="province_id.country_id")
    street2 = fields.Char(related="barangay_id.name")
    name = fields.Char(string="Name")
    city = fields.Char(related="city_municipality_id.name")
    zip = fields.Char(related="street_id.zipcode")
    state_id = fields.Many2one(related="province_id.province_id")
    birthday = fields.Date(string="Birthday",comodel_name="bmis_resident.personal_detail")
    civil_status = fields.Selection(string="Civil Status",selection=[('single','Single'),('married','Married'),('widowed','Widowed')], comodel_name="bmis_resident.personal_detail")
    

    api.onchange("first_name","middle_name","last_name")
    def _onchange_first_name(self):
        if self.first_name and self.last_name:
            self.name = str(self.first_name) + ' ' + str(self.last_name)    
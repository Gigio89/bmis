# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, modules,fields
from datetime import date,datetime,timedelta
from dateutil.relativedelta import relativedelta

class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    first_name = fields.Char(string="First Name",required=True)
    last_name = fields.Char(string="Last Name",required=True)
    middle_name = fields.Char(string="Middle Name")
    parent_id = fields.Many2one(string="Family Head",comodel_name="res.partner")
    household_type = fields.Selection(string='Household Type',
        selection=[('head','Household Head'),('member','Household member')],required=True)
    #company_type = fields.Selection(selection_add=[('member','Member'),('head','Head')], compute='_compute_company_type',inverse='_write_company_type')
    street_id = fields.Many2one(string="Street",comodel_name="bmis.street")
    village_subdivision_id = fields.Many2one(string="Village/Subdibvision",related="street_id.village_subdivision_id")
    barangay_id = fields.Many2one(string="Barangay",related="street_id.barangay_id")
    city_municipality_id = fields.Many2one(string="City-Municipality",related="barangay_id.city_municipality_id",readonly=True)
    province_id = fields.Many2one(string="Province",related="city_municipality_id.province_id")
    country_id = fields.Many2one(string="Country", related="province_id.country_id")
    street2 = fields.Char(related="barangay_id.name",string="Barangay")
    city = fields.Char(related="city_municipality_id.name",string="City/Municipality")
    zip = fields.Char(related="street_id.zipcode",string="Zipcode")
    state_id = fields.Many2one(related="province_id.province_id",string="Province/State")
    birthday = fields.Date(string="Birthday",comodel_name="bmis_resident.personal_detail")
    civil_status = fields.Selection(string="Civil Status",selection=[('single','Single'),('married','Married'),('widowed','Widowed')], comodel_name="bmis_resident.personal_detail")
    gender = fields.Selection(string="Gender", comodel_name="bmis_resident.personal_detail",selection=[('male','Male'),('female','Female')])
    age = fields.Integer(string="Age",store=True, readonly=True)
    test = fields.Char(string="test",store=True)
    
    
    @api.onchange("first_name","middle_name","last_name")
    def _onchange_first_name(self):
        for record in self:
            if record.first_name and record.last_name:
                record.name = str(record.first_name) + ' ' + str(record.middle_name) + ' ' + str(record.last_name)
                
    @api.onchange("birthday")
    def _get_age(self):
        for record in self:
            if record.birthday:
                bd = record.birthday
                age = date.today().year - bd.year
                record.age = str(age)
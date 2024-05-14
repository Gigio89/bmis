# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, modules,fields
from datetime import date

class PersonalDetails(models.Model):
    _name = 'bmis_resident.personal_details'
    _description = 'Residents Personal Details'

    name = fields.Char(string="Name",required=True)
    age = fields.Int(string="Age",required=True)
    birthday = fields.Date(string="Birthday")
    resident_type = fields.Selection(string='Unit Type',
    selection=[('owner','Unit Owner'),('tenant','Unit Tenant'),('business','Business')],required=True)
    gender = fields.Selection(string="Street",selection=[('male','Male'),('femail','Femail')])
    res_partner_id = fields.Many2one(string="Resident", comodel_name="bmis_resident.res_partner")
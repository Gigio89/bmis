# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, modules,fields
from datetime import date

class PersonalDetail(models.Model):
    _name = 'bmis_resident.personal_detail'
    _description = 'Residents Personal Detail'

    name = fields.Char(string="Name")
    birthday = fields.Date(string="Birthday")
    gender = fields.Selection(string="Gender",selection=[('male','Male'),('female','Female')])
    civil_status = fields.Selection(string="Civil Status",selection=[('single','Single'),('married','Married'),('widowed','Widowed')])
    
from odoo import fields, models

class Region(models.Model):
    _name = "bmis.region"
    _description = "List of Regions in the Philippines"

    name = fields.Char(string="Region", required=True)
    description = fields.Text(string="Description", required=True)
    parent_area = fields.Char(string="Area", required=True)
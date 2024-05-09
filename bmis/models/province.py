from odoo import fields, models

class Province(models.Model):
    _name = "bmis.province"
    _description = "List of province in the Philippines"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description", required=True)
    region_id = fields.Many2one(string="Region", comodel_name="bmis.region", required=True)
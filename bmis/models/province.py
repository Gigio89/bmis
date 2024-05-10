from odoo import fields, models

class Province(models.Model):
    _name = "bmis.province"
    _description = "List of province in the Philippines"

    name = fields.Char(string="Name", required=True, related="province_id.name")
    description = fields.Text(string="Description", required=False)
    province_id = fields.Many2one(string="Province", comodel_name="res.country.state", required=True)
    country_id = fields.Many2one(string="Country", related="province_id.country_id", required=True)
    #region_id = fields.Many2one(string="Region", comodel_name="bmis.region", required=True)
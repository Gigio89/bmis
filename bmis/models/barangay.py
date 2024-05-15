from odoo import fields, models

class Barangay(models.Model):
    _name = "bmis.barangay"
    _description = "List of barangays in the city municipality"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    zipcode = fields.Char(string="Zip Code", related="city_municipality_id.zipcode", required=True)
    city_municipality_id = fields.Many2one(string="City/Municipality", comodel_name="bmis.city_municipality", required=True)
    province_id = fields.Many2one(string="Province", related="city_municipality_id.province_id", required=True)
    country_id = fields.Many2one(string="Country", related="province_id.country_id", required=True)
    #region_id = fields.Many2one(string="Region", related="province_id.region_id", required=True)
    is_default = fields.Boolean(strihg="Is Default")
    country_name = fields.Char(related="country_id.name")
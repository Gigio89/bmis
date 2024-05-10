from odoo import fields, models

class CityMunicipality(models.Model):
    _name = "bmis.city_municipality"
    _description = "List of City Municipality in the Philippines"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    zipcode = fields.Char(string="Zip Code", required=True)
    province_id = fields.Many2one(string="Province", comodel_name="bmis.province", required=True)
    country_id = fields.Many2one(string="Country", related="province_id.country_id", required=True) 
    #region_id = fields.Many2one(string="Region", related="province_id.region_id", required=True)
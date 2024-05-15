from odoo import fields, models

class Street(models.Model):
    _name = "bmis.street"
    _description = "List of streets in the barangay"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    
    village_subdivision_id = fields.Many2one(string="Village/Subdivision", comodel_name="bmis.village_subdivision", required=False)
    barangay_id = fields.Many2one(string="Barangay", related="village_subdivision_id.barangay_id", required=True)
    city_municipality_id = fields.Many2one(string="City/Municipality", related="barangay_id.city_municipality_id", required=False)
    zipcode = fields.Char(string="Zip Code", related="city_municipality_id.zipcode", required=False)    
    province_id = fields.Many2one(string="Province", related="city_municipality_id.province_id", required=False)
    country_id = fields.Many2one(string="Country", related="province_id.country_id", required=False)
   # region_id = fields.Many2one(string="Region", related="province_id.region_id", required=True)
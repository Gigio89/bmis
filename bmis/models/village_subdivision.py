from odoo import fields, models

class VillageSubdivision(models.Model):
    _name = "bmis.village_subdivision"
    _description = "List of villages or subdivisions in the barangay"

    name = fields.Char(string="Village/Subdivision", required=True)
    description = fields.Text(string="Description")
    barangay_id = fields.Many2one(string="Barangay", comodel_name="bmis.barangay", required=True)
    
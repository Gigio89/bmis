from odoo import fields, models

class Resident(models.Model):
    _name = "bmis.resident"
    _description = "Residents Module"

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    middle_name = fields.Char(string="Middle Name", required=False)
    active = fields.Boolean(string="Active", default=True)
    addr_detailed = fields.Char(string="Detailed address", required=False)
    addr_street = fields.Char(string="Street", required=False)
    addr_barangay = fields.Char(string="Barangay", default="Brgy. Mariano Espeleta 1")
    addr_city = fields.Char(string="City", default="Imus City")
    addr_province = fields.Char(string="Province", default="Cavite")
    addr_country = fields.Char(string="Country", default="Philippines")
    addr_zip = fields.Char(string="Zip", default="4103")
    res_type = fields.Selection(string="Type of Residency",
                                selection=[
                                    ('owner', 'Owner'),
                                    ('tenant', 'Tenant'),
                                    ('business', 'Business'),
                                ],
                                copy=False)
    profile_picture = fields.Binary('Profile Picture')

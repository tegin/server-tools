# Copyright 2020 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ResUsers(models.Model):

    _inherit = 'res.users'

    google_calendar_id = fields.Char(
        'Google Calendar id',
    )

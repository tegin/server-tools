# Copyright 2020 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Google Calendar Name',
    'summary': """
        Set all google calendar elements to a especific calendar""",
    'version': '11.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Creu Blanca,Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/server-tools',
    'depends': [
        'google_calendar',
    ],
    'data': [
        'views/res_config_settings.xml',
    ],
}

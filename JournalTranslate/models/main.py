from odoo import models, fields, api, _

class my_journal(models.Model):
    _inherit = 'account.journal'
    name = name = fields.Char(string='Journal Name', required=True, translate=True)

class my_account(models.Model):
    _inherit = 'account.account'
    name = fields.Char(string="Account Name", required=True, index=True, translate=True)

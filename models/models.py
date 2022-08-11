# -*- coding: utf-8 -*-

import string
from odoo import models, fields, api


class Visit(models.Model):
    _name = 'custom_crm.visit'
    _description = 'Visit'

    name = fields.Char(string='Description')
    customer = fields.Char(string='Cliente')
    date = fields.Datetime(string='Date')
    type = fields.Selection([('P','Presencial'),('w','WhatsApp'),('T','Telephone')],string='type',required=True)
    done = fields.Boolean(string='Realizado', readonly=True)


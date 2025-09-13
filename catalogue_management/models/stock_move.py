# -*- coding: utf-8 -*-

from odoo import models, fields


class StockMove(models.Model):
    _inherit = "stock.move"

    catalogue_id = fields.Many2one('catalogue.management.line', 'Catalogue')
    assign_to_salesperson = fields.Boolean('Assign to Salesperson', default=False)
    assign_to_customer = fields.Boolean('Assign to Customer', default=False)
    catalogue_info_processed = fields.Boolean(string='Catalogue Info Processed', default=False)

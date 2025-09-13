# -*- coding: utf-8 -*-

from odoo import api, models, fields


class CatalogueProduct(models.Model):
    _name = "catalogue.product"
    _description = 'Catalogue Product'
    _rec_name = 'product_id'
    _order = 'id'

    catalogue_mgmt_id = fields.Many2one('catalogue.management')
    product_id = fields.Many2one('product.product', 'Product')
    quantity = fields.Float(default=1)

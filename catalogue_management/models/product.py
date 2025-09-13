# -*- coding: utf-8 -*-

from odoo import api, models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_catalogue = fields.Boolean(default=False, string="Is Catalogue")


class ProductCategory(models.Model):
    _inherit = "product.category"

    product_catalogue = fields.Many2one('product.template', string="Product Catalogue")
    partner_ids = fields.Many2many('res.partner', string='Customers', compute='_display_partner')

    def _display_partner(self):
        for rec in self:
            if rec.product_catalogue:
                sml_partner_ids = self.env["stock.move.line"].search(
                    [('state', '=', 'done'), ('location_dest_id.usage', '=', 'customer'),
                     ('product_id.product_tmpl_id', '=', rec.product_catalogue.id)]).mapped('picking_partner_id')
                rec.partner_ids = sml_partner_ids
            else:
                rec.partner_ids = False

class Product(models.Model):
    _inherit = "product.product"

    @api.depends('qty_available', 'name')
    def _compute_display_name(self):
        if self.env.context.get('show_on_hand'):
            for product in self:
                product.display_name = f"{product.name} [{product.qty_available}]"
        else:
            return super()._compute_display_name()

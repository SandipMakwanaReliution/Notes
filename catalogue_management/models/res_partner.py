# -*- coding: utf-8 -*-

from odoo import api, models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    category_ids = fields.Many2many('product.category', string='Product Category & Catalogue',
                                    compute='_display_category')
    catalogue_line_ids = fields.One2many('catalogue.management.line', 'partner_id', 'Catalogues Lines', store=True)
    location_id = fields.Many2one('stock.location')

    def _display_category(self):
        for rec in self:
            sm_lines = self.env["stock.move.line"].search([
                ('state', '=', 'done'), ('picking_partner_id', '=', rec.id), ('location_dest_id.usage', '=', 'customer')
            ])
            vals = []
            if sm_lines:
                for line in sm_lines:
                    if line.product_id.product_tmpl_id.is_catalogue:
                        vals.append(line.product_id.product_tmpl_id.categ_id.id)
                rec.category_ids = vals
            else:
                rec.category_ids = False

# -*- coding: utf-8 -*-

from odoo import api, models, fields


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    product_category = fields.Many2one('product.category', string="Product Category", store=True,
                                       compute='_compute_product_categ')
    product_catalogue = fields.Many2one('product.template', string="Product Catalogue", store=True,
                                        compute='_compute_product_catalogue')
    catalogue_id = fields.Many2one('catalogue.management.line', string='Catalogue',
                                   compute='_compute_catalogue_id', store=True)
    catalogue_info_id =  fields.Many2one('catalogue.info', string='Catalogue Info',
                                   compute='_compute_catalogue_id', store=True)
    quality = fields.Selection([
        ('blackout', 'Blackout'),
        ('sheer', 'Sheer'),
        ('velvet', 'Velvet'),
        ('satin', 'Satin'),
        ('upholstery', 'Upholstery'),
        ('boucle', 'Boucle')
    ], string="Quality", store=True, compute='_compute_product_quality')

    @api.depends('product_template_id', 'product_template_id.categ_id')
    def _compute_product_categ(self):
        for rec in self:
            product_category = False
            if rec.product_template_id.categ_id:
                product_category = rec.product_template_id.categ_id
            rec.product_category = product_category

    @api.depends('product_template_id', 'product_template_id.quality')
    def _compute_product_quality(self):
        for rec in self:
            quality = False
            if rec.product_template_id.quality:
                quality = rec.product_template_id.quality
            rec.quality = quality

    @api.depends('product_template_id', 'product_template_id.categ_id',
                 'product_template_id.categ_id.product_catalogue', 'order_partner_id', 'order_partner_id.category_ids')
    def _compute_product_catalogue(self):
        for rec in self:
            product_catalogue = False
            if rec.product_template_id.categ_id:
                categ_id = rec.product_template_id.categ_id
                if categ_id in rec.order_partner_id.category_ids:
                    product_catalogue = rec.product_template_id.categ_id.product_catalogue
            rec.product_catalogue = product_catalogue

    @api.depends('product_uom_qty', 'product_template_id', 'price_subtotal', 'qty_delivered', 'qty_invoiced')
    def _compute_catalogue_id(self):
        for rec in self:
            catalogue_id = False
            catalogue_line = self.env['catalogue.management.line'].search([
                ('partner_id', '=', rec.order_partner_id.id), ('categ_id', '=', rec.product_id.categ_id.id)], limit=1)
            if catalogue_line:
                catalogue_id = catalogue_line
            rec.catalogue_id = catalogue_id

            catalogue_info_line = self.env['catalogue.info'].search([
                ('user_id', '=', rec.salesman_id.id),
                ('customer_id', '=', rec.order_partner_id.id),
                ('catalogues_category_id', '=', rec.product_id.categ_id.id)], limit=1)
            rec.catalogue_info_id = catalogue_info_line if catalogue_info_line else False

    def action_compute_catalogue_ids(self):
        self.env['catalogue.info'].sudo().generate_catalogue_info()
        order_lines = self.search(['|', ('catalogue_id', '=', False), ('catalogue_info_id', '=', False)])
        order_lines._compute_catalogue_id()

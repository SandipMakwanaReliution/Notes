# -*- coding: utf-8 -*-

from odoo import api, models, fields


class CatalogueManagementLine(models.Model):
    _name = "catalogue.management.line"
    _description = 'Catalogue Management Line'
    _rec_name = 'display_name'

    partner_id = fields.Many2one('res.partner', 'Customer')
    area = fields.Many2one('res.area', 'Area', compute='_compute_area', store=True)
    categ_id = fields.Many2one('product.category', 'Category', related='product_tmpl_id.categ_id')
    product_id = fields.Many2one('product.product', 'Product Variant', related='product_tmpl_id.product_variant_id')
    product_tmpl_id = fields.Many2one('product.template', 'Catalogue', domain="[('is_catalogue', '=', True)]")
    move_ids = fields.One2many('stock.move', 'catalogue_id')
    no_of_catalogue = fields.Float('Catalogues', compute='_compute_no_of_catalogue', store=True)
    sale_order_line_ids = fields.One2many('sale.order.line', 'catalogue_id')
    no_of_sale_orders = fields.Float('Sale Orders', compute='_compute_sale_order_info', store=True)
    total_ordered_qty = fields.Float('Ordered Qty', compute='_compute_sale_order_info', store=True)
    total_delivered_qty = fields.Float('Delivered Qty', compute='_compute_sale_order_info', store=True)
    total_invoiced_qty = fields.Float('Invoiced Qty', compute='_compute_sale_order_info', store=True)
    total_untaxed_amount = fields.Float('Untaxed Amount', compute='_compute_sale_order_info', store=True)
    user_id = fields.Many2one('res.users', 'Salesperson', compute='_compute_user_id', store=True)
    display_name = fields.Char('Display Name', compute='_compute_display_name')
    assign_to_salesperson = fields.Boolean('Assign to Salesperson', default=False)
    assign_to_customer = fields.Boolean('Assign to Customer', default=False)

    @api.depends('move_ids', 'move_ids.product_uom_qty', 'move_ids.partner_id', 'move_ids.product_id')
    def _compute_no_of_catalogue(self):
        for rec in self:
            no_of_catalogue = 0
            if rec.move_ids:
                no_of_catalogue = sum(rec.move_ids.mapped('product_uom_qty'))
            rec.no_of_catalogue = no_of_catalogue

    @api.depends('sale_order_line_ids', 'sale_order_line_ids.product_uom_qty', 'sale_order_line_ids.qty_delivered',
                 'sale_order_line_ids.qty_invoiced')
    def _compute_sale_order_info(self):
        for rec in self:
            total_sale_orders = 0
            total_ordered_qty = 0
            total_delivered_qty = 0
            total_invoiced_qty = 0
            total_amount = 0
            if rec.sale_order_line_ids:
                order_lines = rec.sale_order_line_ids.filtered(lambda l: l.state == 'sale')
                total_sale_orders = len(order_lines.mapped('order_id'))
                total_ordered_qty = sum(order_lines.mapped('product_uom_qty'))
                total_delivered_qty = sum(order_lines.mapped('qty_delivered'))
                total_invoiced_qty = sum(order_lines.mapped('qty_invoiced'))
                total_amount = sum((order_lines.mapped('price_subtotal')))
            rec.no_of_sale_orders = total_sale_orders
            rec.total_ordered_qty = total_ordered_qty
            rec.total_delivered_qty = total_delivered_qty
            rec.total_invoiced_qty = total_invoiced_qty
            rec.total_untaxed_amount = total_amount

    @api.depends('partner_id', 'partner_id.area')
    def _compute_area(self):
        for rec in self:
            rec.area = rec.partner_id.area

    @api.depends('partner_id', 'partner_id.user_id')
    def _compute_user_id(self):
        for rec in self:
            rec.user_id = rec.partner_id.user_id if rec.partner_id.user_id else self.env.user

    def _compute_display_name(self):
        for rec in self:
            display_name = "{}[{}]".format(rec.partner_id.name, rec.categ_id.product_catalogue.name)
            rec.display_name = display_name

    def action_stock_moves(self):
        action = self.env["ir.actions.act_window"]._for_xml_id("stock.stock_move_action")

        stock_moves = self.env['stock.move'].search([('catalogue_id', '=', self.id)])

        action['domain'] = [('id', 'in', stock_moves.ids)]
        return action

    def action_sale_order_lines(self):
        action = self.env["ir.actions.act_window"]._for_xml_id("catalogue_management.action_orders_lines_pivot")

        order_lines = self.env['sale.order.line'].search([('catalogue_id', '=', self.id)])

        action['domain'] = [('id', 'in', order_lines.ids)]

        return action

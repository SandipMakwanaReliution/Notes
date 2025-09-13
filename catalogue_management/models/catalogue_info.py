# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Dashboard(models.Model):
    _name = 'catalogue.info'
    _description = 'Catalogue Information'

    salesperson_id = fields.Many2one('res.partner', string='Salesperson')
    user_id = fields.Many2one('res.users', string='Salesperson User')
    catalogues = fields.Many2one('product.product', string='Catalogues')
    catalogues_category_id = fields.Many2one('product.category', 'Catalogues Category', related='catalogues.categ_id')
    cata_assign_to_salesperson = fields.Float(string='Assign to Salesperson')
    salesperson_cata_ava_qty = fields.Float(string='Available Quantity')
    customer_id = fields.Many2one('res.partner', string='Customer')
    customer_count = fields.Float('Customer Count', compute='_compute_customer_count', store=True)
    cata_assign_to_customer = fields.Float(string='Assign to Customer')
    label = fields.Char(string="Label")
    sale_order_line_ids = fields.One2many('sale.order.line', 'catalogue_info_id')
    no_of_sale_orders = fields.Float('Sale Orders', compute='_compute_sale_order_info', store=True)
    total_ordered_qty = fields.Float('Ordered Qty', compute='_compute_sale_order_info', store=True)
    total_delivered_qty = fields.Float('Delivered Qty', compute='_compute_sale_order_info', store=True)
    total_invoiced_qty = fields.Float('Invoiced Qty', compute='_compute_sale_order_info', store=True)
    total_untaxed_amount = fields.Float('Untaxed Amount', compute='_compute_sale_order_info', store=True)

    @api.depends('cata_assign_to_salesperson', 'cata_assign_to_customer', 'salesperson_cata_ava_qty', 'customer_id')
    def _compute_customer_count(self):
        salespersons = self.env['res.partner'].search([('location_id', '!=', False)])
        for salesperson in salespersons:
            user = salesperson.user_ids[:1] if salesperson.user_ids else False
            total = self.search([('user_id', '=', user.id), ('customer_id', '!=', False)])
            customer_count = len(total.mapped('customer_id'))
            for rec in total:
                rec.write({'customer_count': customer_count})

    @api.model
    def generate_catalogue_info(self):
        salespersons = self.env['res.partner'].search([('location_id', '!=', False)])

        for salesperson in salespersons:
            salesperson_location = salesperson.location_id
            user = salesperson.user_ids[:1] if salesperson.user_ids else False

            assign_to_salesperson_moves = self.env['stock.move'].search([
                ('assign_to_salesperson', '=', True),
                ('location_dest_id', '=', salesperson_location.id),
                ('catalogue_info_processed', '=', False)
            ])
            for move in assign_to_salesperson_moves:
                salesperson_dashboard_data = self.env['catalogue.info'].search([
                    ('salesperson_id','=',salesperson.id),
                    ('label','=','Assign to Salesperson'),
                    ('catalogues','=',move.product_id.id)
                ],limit=1)
                if salesperson_dashboard_data:
                    salesperson_dashboard_data.cata_assign_to_salesperson += move.quantity
                else:
                    self.create({
                        'salesperson_id': salesperson.id,
                        'user_id': user.id if user else False,
                        'customer_id': False,
                        'catalogues': move.product_id.id,
                        'cata_assign_to_salesperson': move.quantity,
                        'salesperson_cata_ava_qty': 0.0,
                        'cata_assign_to_customer': 0.0,
                        'label': 'Assign to Salesperson',
                    })
                move.write({'catalogue_info_processed': True})

            available_quants = self.env['stock.quant'].search([
                ('location_id', '=', salesperson_location.id),
            ])
            for quant in available_quants:
                available_dashboard_data = self.env['catalogue.info'].search([
                    ('salesperson_id', '=', salesperson.id),
                    ('label', '=', 'Available'),
                    ('catalogues', '=', quant.product_id.id)
                ], limit=1)
                if available_dashboard_data:
                    available_dashboard_data.salesperson_cata_ava_qty = quant.quantity
                else:
                    self.create({
                        'salesperson_id': salesperson.id,
                        'user_id': user.id if user else False,
                        'customer_id': False,
                        'catalogues': quant.product_id.id,
                        'cata_assign_to_salesperson': 0.0,
                        'salesperson_cata_ava_qty': quant.quantity,
                        'cata_assign_to_customer': 0.0,
                        'label': 'Available',
                    })

            assign_to_customer_moves = self.env['stock.move'].search([
                ('assign_to_customer','=',True),
                ('location_id','=',salesperson_location.id),
                ('catalogue_info_processed', '=', False)
            ])
            for move in assign_to_customer_moves:
                customer_dashboard_data = self.env['catalogue.info'].search([
                    ('salesperson_id','=',salesperson.id),
                    ('customer_id','=',move.catalogue_id.partner_id.id),
                    ('catalogues','=',move.product_id.id)
                ],limit=1)

                if customer_dashboard_data:
                    customer_dashboard_data.cata_assign_to_customer += move.quantity
                else:
                    self.create({
                        'salesperson_id': salesperson.id,
                        'user_id': user.id if user else False,
                        'customer_id': move.catalogue_id.partner_id.id,
                        'catalogues': move.product_id.id,
                        'cata_assign_to_salesperson': 0.0,
                        'salesperson_cata_ava_qty': 0.0,
                        'cata_assign_to_customer': move.quantity,
                        'label': 'Assign to Customer',
                    })
                move.write({'catalogue_info_processed': True})

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

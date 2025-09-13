# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.exceptions import ValidationError


class CatalogueManagement(models.Model):
    _name = "catalogue.management"
    _description = 'Catalogue Management'
    _rec_name = 'partner_id'
    _order = 'id'

    partner_id = fields.Many2one('res.partner', 'Customer')
    all_partner_id = fields.Many2one('res.partner', 'Customer')
    salesperson_id = fields.Many2one('res.partner', 'Salesperson')
    catalogue_ids = fields.Many2many('product.product', string="Catalogues")
    catalogue_product_ids = fields.One2many('catalogue.product', 'catalogue_mgmt_id')
    user_id = fields.Many2one('res.users', 'User', default=lambda self: self.env.user)
    picking_id = fields.Many2one('stock.picking', 'Picking')

    def create_catalogue_picking(self):
        move_lines = []
        if self.salesperson_id and not self.salesperson_id.location_id:
            raise ValidationError('Please set the location of salesperson.')
        if self.partner_id and not self.user_id.partner_id.location_id:
            raise ValidationError("Please set the location of current user contact.")
        if self.all_partner_id and not self.user_id.partner_id.location_id:
            raise ValidationError("Please set the location of current user contact.")
        partner = self.env['res.partner']
        if self.partner_id:
            partner = self.partner_id
        if self.all_partner_id:
            partner = self.all_partner_id

        for line in self.catalogue_product_ids:
            if line.quantity > 0:
                customer_catalogue = self.env['catalogue.management.line'].search([
                    ('partner_id', '=', partner.id), ('assign_to_customer', '=', True),
                    ('product_tmpl_id', '=', line.product_id.product_tmpl_id.id)], limit=1)
                salesperson_catalogue = self.env['catalogue.management.line'].search([
                    ('partner_id', '=', self.salesperson_id.id), ('assign_to_salesperson', '=', True),
                    ('product_tmpl_id', '=', line.product_id.product_tmpl_id.id)], limit=1)
                if customer_catalogue:
                    catalogue_id = customer_catalogue
                elif salesperson_catalogue:
                    catalogue_id = salesperson_catalogue
                else:
                    catalogue_id = self.env['catalogue.management.line'].create({
                        'partner_id': partner.id or self.salesperson_id.id,
                        'product_tmpl_id': line.product_id.product_tmpl_id.id,
                        'assign_to_salesperson': True if self.salesperson_id else False,
                        'assign_to_customer': True if partner else False,
                    })
                vals = (0, 0, {
                    'name': line.product_id.name,
                    'product_id': line.product_id.id,
                    'product_uom': line.product_id.uom_id.id,
                    'partner_id': self.salesperson_id.id or partner.id,
                    'product_uom_qty': line.quantity,
                    'quantity': line.quantity,
                    'location_id': self.user_id.partner_id.location_id.id if partner else self.env.ref('stock.stock_location_stock').id,
                    'location_dest_id': self.salesperson_id.location_id.id if self.salesperson_id else self.env.ref('stock.stock_location_customers').id,
                    'catalogue_id': catalogue_id.id,
                    'assign_to_salesperson': True if self.salesperson_id else False,
                    'assign_to_customer': True if partner else False,
                })
                move_lines.append(vals)
            else:
                raise ValidationError('Enter at least 1 quantity to distribute catalogue.')
        if move_lines:
            picking = self.env['stock.picking'].create({
                'partner_id': self.salesperson_id.id or partner.id,
                'picking_type_id': self.env.ref('stock.picking_type_out').id,
                'location_id': self.user_id.partner_id.location_id.id if partner else self.env.ref('stock.stock_location_stock').id,
                'location_dest_id': self.salesperson_id.location_id.id if self.salesperson_id else self.env.ref('stock.stock_location_customers').id,
                'move_ids': move_lines,
            })
            self.write({
                'picking_id': picking.id
            })
            picking.button_validate()

        self.env['catalogue.info'].sudo().generate_catalogue_info()

    def catalogue_report(self):
        return self.env.ref('catalogue_management.report_catalogue_pdf').report_action(self)

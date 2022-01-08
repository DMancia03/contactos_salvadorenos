# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

# Indicacion
# Añadir el campo de sucursales a los clientes, el cual deberá de ser cargado en
# el pedido de venta cada vez que un cliente sea seleccionado.

class SaleOrderExtend(models.Model):
    # Clase heredada sale.order
    _inherit='sale.order'

    sucursal_id = fields.Many2one('contact.sucursal', string='Sucursal') # Sucursal del contacto

    # Onchange para hacer la asignacion automatica de sucursal
    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        sucursales = []
        self.sucursal_id = [(5,0,0)]

        if self.partner_id:
            for i in self.partner_id.sucursal_id:
                # Se valida por si el cliente no tiene sucursal asignada
                if i:
                    self.sucursal_id = i
            #_logger = logging.getLogger(sucursal)
            
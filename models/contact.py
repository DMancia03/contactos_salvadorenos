# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

# Indicacion
# Es necesario dotar a Odoo Versión 14 Community de campos para poder
# registrar los contactos con mas detalles acerca de las leyes salvadoreñas

class ContactSalvadorenoExtend(models.Model):
    # Clase heradada: res.partner
    _inherit = 'res.partner'

    #Campos
    dui = fields.Char(string='DUI', size=9, required=True) # Dui
    nit = fields.Char(string='NIT', size=17, required=False) # Nit
    nrc = fields.Char(string='NRC', required=False) # Nrc
    # Para filtrar las sucursales ocupe un domain
    sucursal_id = fields.Many2one('contact.sucursal', string='Sucursal', domain="[('company_id','=',company_id)]", required=True)

    # Al principio habia usado un onchange con un domain, que no me funciono
    #@api.onchange('company_id')
    #def _onchange_company_id(self):
    #   if self.company_id:
    #       domain = {'sucursal_id': [('company_id', '=', self.company_id)]}
    #       return {'domain':domain}

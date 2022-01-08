# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

# Indicacion
# Se necesita tener la posibilidad de crear sucursales por compañía y asignarlas
# a los contactos al momento de su creación

class ContactSucursal(models.Model):
    _name = "contact.sucursal"
    _description = "Modelo para crear sucursales por compañía"

    name = fields.Char(string='Nombre', required=True) # Nombre
    short_name = fields.Char(string='Nombre corto', required=True) # Nombre corto
    company_id = fields.Many2one('res.company', string='Compañía', required=True) # Compañia
from odoo import models, fields

class Persona(models.Model):
    _name = 'taller.persona'
    _description = 'Personas en el taller'

    nif = fields.Char('NIF', required=True)
    nombre = fields.Char('Nombre', required=True)
    correo = fields.Char('Correo Electrónico')
    direccion = fields.Char('Dirección')
    telefono = fields.Char('Teléfono')
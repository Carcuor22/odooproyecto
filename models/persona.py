from odoo import models, fields

class Persona(models.Model):
    _name = 'odooproyecto.persona'
    _description = 'Persona'

    nif = fields.Char(string="NIF", required=True)
    nombre = fields.Char(string="Nombre", required=True)
    correo = fields.Char(string="Correo Electrónico")
    direccion = fields.Char(string="Dirección")
    telefono = fields.Integer(string="Teléfono")

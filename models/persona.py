from odoo import models, fields

class Persona(models.Model):
    _name = 'odooproyecto.persona'
    _description = 'Persona'
    
    nif = fields.Char(string="NIF", required=True, index=True)  # Solo índice, no 'unique' si se usa _inherits
    nombre = fields.Char(string="Nombre", required=True)
    correo = fields.Char(string="Correo")
    direccion = fields.Char(string="Dirección")
    telefono = fields.Char(string="Teléfono")
    
    _sql_constraints = [
        ('persona_nif_unique', 'unique(nif)', 'El NIF debe ser único.')
    ]

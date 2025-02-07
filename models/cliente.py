from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'odooproyecto.cliente'
    _description = 'Cliente'
    _inherits = {'odooproyecto.persona': 'nif'}  # Hereda los atributos de Persona

    nif = fields.Char(string="NIF", required=True, ondelete='cascade')  # Relacionado con Persona
    tipo = fields.Selection([
        ('empresa', 'Empresa'),
        ('particular', 'Particular'),
        ('junta', 'Junta Andalucía'),
        ('organismo', 'Organismo Público'),
    ], string="Tipo de Cliente")

from odoo import models, fields

class Cliente(models.Model):
    _name = 'odooproyecto.cliente'
    _description = 'Cliente'
    _inherits = {'odooproyecto.persona': 'nif'}

    nif = fields.Many2one('odooproyecto.persona', string="NIF", required=True, ondelete='cascade')  # Relacionado con Persona
    tipo = fields.Selection([
        ('empresa', 'Empresa'),
        ('particular', 'Particular'),
        ('junta', 'Junta Andalucía'),
        ('organismo', 'Organismo Público'),
    ], string="Tipo de Cliente")

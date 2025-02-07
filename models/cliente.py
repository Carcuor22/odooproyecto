from odoo import models, fields

class Cliente(models.Model):
    _name = 'odooproyecto.cliente'
    _description = 'Cliente'
    _inherits = {'odooproyecto.persona': 'persona_id'}

    persona_id = fields.Many2one('odooproyecto.persona', string="Persona", required=True, ondelete="cascade")
    tipo = fields.Selection([
        ('empresa', 'Empresa'),
        ('particular', 'Particular'),
        ('junta', 'Junta Andalucía'),
        ('organismo', 'Organismo Público'),
    ], string="Tipo de Cliente")

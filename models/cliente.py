from odoo import models, fields

class Cliente(models.Model):
    _name = 'taller.cliente'
    _description = 'Clientes del taller'
    _inherits = {'taller.persona': 'persona_id'}  # ← Usamos persona_id en lugar de nif

    persona_id = fields.Many2one('taller.persona', required=True, ondelete='cascade')  # ← Cambiado a Many2one
    tipo = fields.Selection([
        ('empresa', 'Empresa'),
        ('particular', 'Particular'),
        ('junta', 'Junta Andalucía'),
        ('organismo', 'Organismo Público')
    ], string='Tipo')

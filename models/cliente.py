from odoo import models, fields

class Cliente(models.Model):
    _name = 'odooproyecto.cliente'
    _description = 'Cliente'
    _inherits = {'odooproyecto.persona': 'persona_id'}

<<<<<<< HEAD
    persona_id = fields.Many2one('odooproyecto.persona', string="Persona", required=True, ondelete="cascade")
=======
    nif = fields.Many2one('odooproyecto.persona', string="NIF", required=True, ondelete='cascade')  # Relacionado con Persona
>>>>>>> 2b0bbfc0f506241ca5885824b39010173ff03805
    tipo = fields.Selection([
        ('empresa', 'Empresa'),
        ('particular', 'Particular'),
        ('junta', 'Junta Andalucía'),
        ('organismo', 'Organismo Público'),
    ], string="Tipo de Cliente")

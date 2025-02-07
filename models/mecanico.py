from odoo import models, fields

class Mecanico(models.Model):
    _name = 'odooproyecto.mecanico'
    _description = 'Mecanico'
    _inherits = {'odooproyecto.persona': 'persona_id'}

<<<<<<< HEAD
    persona_id = fields.Many2one('odooproyecto.persona', string="Persona", required=True, ondelete="cascade")
=======
    nif = fields.Many2one('odooproyecto.persona', string="NIF", required=True, ondelete='cascade')  # Relacionado con Persona
>>>>>>> 2b0bbfc0f506241ca5885824b39010173ff03805
    especializacion = fields.Selection([
        ('mecanica', 'Mecánica'),
        ('electricidad', 'Electricidad'),
        ('pintura', 'Pintura'),
    ], string="Especialización")
    salario = fields.Float(string="Salario")
    foto = fields.Binary(string="Foto")
    fecha_contratacion = fields.Date(string="Fecha de Contratación")

from odoo import models, fields

class Mecanico(models.Model):
    _name = 'odooproyecto.mecanico'
    _description = 'Mecanico'
    _inherits = {'odooproyecto.persona': 'persona_id'}

    persona_id = fields.Many2one('odooproyecto.persona', string="Persona", required=True, ondelete="cascade")
    especializacion = fields.Selection([
        ('mecanica', 'Mecánica'),
        ('electricidad', 'Electricidad'),
        ('pintura', 'Pintura'),
    ], string="Especialización")
    salario = fields.Float(string="Salario")
    foto = fields.Binary(string="Foto")
    fecha_contratacion = fields.Date(string="Fecha de Contratación")

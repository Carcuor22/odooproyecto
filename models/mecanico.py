from odoo import models, fields

class Mecanico(models.Model):
    _name = 'odooproyecto.mecanico'
    _description = 'Mecanico'
    _inherits = {'odooproyecto.persona': 'nif'}

    nif = fields.Many2one('odooproyecto.persona', string="NIF", required=True, ondelete='cascade')  # Relacionado con Persona
    especializacion = fields.Selection([
        ('mecanica', 'Mecánica'),
        ('electricidad', 'Electricidad'),
        ('pintura', 'Pintura'),
    ], string="Especialización")
    salario = fields.Float(string="Salario")
    foto = fields.Binary(string="Foto")
    fecha_contratacion = fields.Date(string="Fecha de Contratación")

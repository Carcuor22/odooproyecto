from odoo import models, fields

class Mecanico(models.Model):
    _name = 'taller.mecanico'
    _description = 'Mecánicos del taller'
    _inherits = {'taller.persona': 'persona_id'}  # Hereda de Persona

    persona_id = fields.Many2one('taller.persona', required=True, ondelete='cascade')
    especializacion = fields.Selection([
        ('motor', 'Motor'),
        ('electricidad', 'Electricidad'),
        ('carroceria', 'Carrocería'),
        ('diagnostico', 'Diagnóstico')
    ], string='Especialización', required=True)
    salario = fields.Float('Salario', required=True)
    fecha_contratacion = fields.Date('Fecha de Contratación', required=True)

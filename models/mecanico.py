from odoo import models, fields

class Mecanico(models.Model):
    _name = 'odooproyecto.mecanico'
    _description = 'Mecanico'
    _inherits = {'odooproyecto.persona': 'nif'}  # Hereda los atributos de Persona

    nif = fields.Char(string="NIF", required=True)  # Relacionado con Persona
    especializacion = fields.Selection([
        ('mecanica', 'Mecánica'),
        ('electricidad', 'Electricidad'),
        ('pintura', 'Pintura'),
    ], string="Especialización")
    salario = fields.Float(string="Salario")
    foto = fields.Binary(string="Foto")
    fecha_contratacion = fields.Date(string="Fecha de Contratación")

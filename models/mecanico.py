from odoo import models, fields

class Mecanico(models.Model):
    _name = 'taller.mecanico'
    _inherit = 'taller.persona'
    _description = 'Mecánico'

    especializacion = fields.Selection(
        [('mecanica', 'Mecánica'),
         ('electricidad', 'Electricidad'),
         ('pintura', 'Pintura')],
        string="Especialización", required=True)
    salario = fields.Float(string="Salario", required=True)
    foto = fields.Binary(string="Foto")
    fecha_contratacion = fields.Date(string="Fecha de Contratación", required=True)

from odoo import models, fields

class Cliente(models.Model):
    _name = 'taller.cliente'
    _inherit = 'taller.persona'
    _description = 'Cliente'

    tipo = fields.Selection(
        [('empresa', 'Empresa'),
         ('particular', 'Particular'),
         ('junta_andalucia', 'Junta Andalucía'),
         ('organismo_publico', 'Organismo Público')],
        string="Tipo de Cliente", required=True)

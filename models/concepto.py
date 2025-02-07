from odoo import models, fields

class Concepto(models.Model):
    _name = 'odooproyecto.concepto'
    _description = 'Conceptos de Reparación'

    descripcion = fields.Char(string="Descripción", required=True)
    precio = fields.Float(string="Precio", required=True)
    mano_obra = fields.Float(string="Mano de Obra", required=True)
    reparacion_id = fields.Many2one('odooproyecto.reparacion', string="Reparación", required=True, ondelete='cascade')dsdsd

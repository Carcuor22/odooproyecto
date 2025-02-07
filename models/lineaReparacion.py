from odoo import models, fields

class LineaReparacion(models.Model):
    _name = 'taller.lineareparacion'
    _description = 'Línea de Reparación'

    cantidad = fields.Integer(string="Cantidad", required=True)
    descripcion = fields.Char(string="Descripción", required=True)
    importe = fields.Float(string="Importe", required=True)
    reparacion_id = fields.Many2one('taller.reparacion', string="Reparación", required=True, ondelete='cascade')

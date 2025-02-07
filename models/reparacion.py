from odoo import models, fields, api

class Reparacion(models.Model):
    _name = 'odooproyecto.reparacion'
    _description = 'Reparación'

    fecha_ini = fields.Datetime(string="Fecha de Inicio", required=True)
    fecha_fin = fields.Datetime(string="Fecha de Fin")
    total = fields.Float(string="Total", compute='_compute_total', store=True)
    descripcion = fields.Text(string="Descripción")
    cliente_id = fields.Many2one('odooproyecto.cliente', string="Cliente", required=True)
    mecanico_ids = fields.Many2many('odooproyecto.mecanico', string="Mecánicos")
    linea_reparacion_ids = fields.One2many('odooproyecto.lineareparacion', 'reparacion_id', string="Líneas de Reparación")
    concepto_ids = fields.One2many('odooproyecto.concepto', 'reparacion_id', string="Conceptos")

    @api.depends('linea_reparacion_ids.importe')
    def _compute_total(self):
        for record in self:
            record.total = sum(linea.importe for linea in record.linea_reparacion_ids)

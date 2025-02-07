from odoo import models, fields, api

class Reparacion(models.Model):
    _name = 'taller.reparacion'
    _description = 'Reparación'

    fecha_ini = fields.Datetime(string="Fecha de Inicio", required=True)
    fecha_fin = fields.Datetime(string="Fecha de Fin")
    total = fields.Float(string="Total", compute='_compute_total', store=True)
    descripcion = fields.Text(string="Descripción")
    cliente_id = fields.Many2one('taller.cliente', string="Cliente", required=True)
    mecanico_ids = fields.Many2many('taller.mecanico', string="Mecánicos")
    linea_reparacion_ids = fields.One2many('taller.lineareparacion', 'reparacion_id', string="Líneas de Reparación")

    @api.depends('linea_reparacion_ids.importe')
    def _compute_total(self):
        for record in self:
            record.total = sum(linea.importe for linea in record.linea_reparacion_ids)

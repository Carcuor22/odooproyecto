from odoo import models, fields

class Reparacion(models.Model):
    _name = 'taller.reparacion'
    _description = 'Reparaciones en el taller'

    id_reparacion = fields.Integer('ID Reparación', required=True)
    fecha_ini = fields.Datetime('Fecha de Inicio', required=True)
    fecha_fin = fields.Datetime('Fecha de Fin', required=True)
    total = fields.Float('Total', required=True)
    descripcion = fields.Text('Descripción')

    # Relación Many2Many con Mecánicos
    mecanicos_ids = fields.Many2many(
        'taller.mecanico',  # Modelo relacionado
        'taller_reparacion_mecanico_rel',  # Nombre de la tabla intermedia
        'reparacion_id',  # Nombre del campo que referencia a `taller.reparacion`
        'mecanico_id',  # Nombre del campo que referencia a `taller.mecanico`
        string='Mecánicos Asignados'
    )

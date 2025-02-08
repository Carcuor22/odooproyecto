from odoo import models, fields

class Mecanico(models.Model):
    _name = 'taller.mecanico'
    _description = 'Mecánicos del taller'
    _inherits = {'taller.persona': 'persona_id'}

    persona_id = fields.Many2one('taller.persona', required=True, ondelete='cascade')
    especializacion = fields.Selection([
        ('motor', 'Motor'),
        ('electricidad', 'Electricidad'),
        ('carroceria', 'Carrocería'),
        ('diagnostico', 'Diagnóstico')
    ], string='Especialización', required=True)
    salario = fields.Float('Salario', required=True)
    fecha_contratacion = fields.Date('Fecha de Contratación', required=True)

    # Relación Many2Many con Reparaciones
    reparaciones_ids = fields.Many2many(
        'taller.reparacion',  # Modelo relacionado
        'taller_reparacion_mecanico_rel',  # Nombre de la tabla intermedia
        'mecanico_id',  # Nombre del campo que referencia a `taller.mecanico`
        'reparacion_id',  # Nombre del campo que referencia a `taller.reparacion`
        string='Reparaciones'
    )

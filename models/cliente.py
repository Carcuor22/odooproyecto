from odoo import models, fields

class Cliente(models.Model):
    _name = 'odooproyecto.cliente'
    _inherit = 'odooproyecto.persona'
    _description = 'Cliente'

    vehiculo_ids = fields.One2many('odooproyecto.vehiculo', 'cliente_id', string="Vehículos")
    reparacion_ids = fields.One2many('odooproyecto.reparacion', 'cliente_id', string="Reparaciones")

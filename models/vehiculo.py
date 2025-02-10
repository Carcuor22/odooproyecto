from odoo import models, fields

class Vehiculo(models.Model):
    _name = 'taller.vehiculo'
    _description = 'Vehículos de clientes'

    matricula = fields.Char('Matrícula', required=True)
    marca = fields.Char('Marca', required=True)
    modelo = fields.Char('Modelo', required=True)
    motor = fields.Char('Motor')

    cliente_id = fields.Many2one('taller.cliente', string='Cliente', ondelete='cascade')

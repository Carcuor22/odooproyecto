from odoo import models, fields

class Vehiculo(models.Model):
    _name = 'taller.vehiculo'
    _description = 'Vehículo'

    matricula = fields.Char(string="Matrícula", required=True)
    marca = fields.Char(string="Marca", required=True)
    modelo = fields.Char(string="Modelo", required=True)
    motor = fields.Selection(
        [('electrico', 'Eléctrico'),
         ('gasolina', 'Gasolina'),
         ('diesel', 'Diésel'),
         ('hibrido', 'Híbrido'),
         ('hibrido_enchufable', 'Híbrido Enchufable')],
        string="Tipo de Motor", required=True)
    foto = fields.Binary(string="Foto")
    cliente_id = fields.Many2one('taller.cliente', string="Cliente", required=True)

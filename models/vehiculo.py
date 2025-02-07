from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Vehiculo(models.Model):
    _name = 'odooproyecto.vehiculo'
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

    # Estado del vehículo
    state = fields.Selection([
        ('disponible', 'Disponible'),
        ('en_reparacion', 'En Reparación'),
        ('reparado', 'Reparado'),
        ('entregado', 'Entregado')
    ], string="Estado", default="disponible")

    @api.constrains('matricula')
    def _check_unique_matricula(self):
        """ Verifica que no haya matrículas duplicadas """
        for record in self:
            existing = self.search([('matricula', '=', record.matricula), ('id', '!=', record.id)])
            if existing:
                raise ValidationError("Ya existe un vehículo con esta matrícula.")

    # Métodos para cambiar de estado
    def iniciar_reparacion(self):
        """ Pasa el vehículo a estado 'En reparación' """
        self.state = 'en_reparacion'

    def finalizar_reparacion(self):
        """ Pasa el vehículo a estado 'Reparado' """
        self.state = 'reparado'

    def entregar_vehiculo(self):
        """ Pasa el vehículo a estado 'Entregado' """
        self.state = 'entregado'

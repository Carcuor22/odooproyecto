{
    'name': "taller_mecanico",
    'summary': "Módulo para gestión de clientes en talleres mecánicos",
    'description': "Gestión de clientes en un taller mecánico con herencia de Persona",
    'author': "Tu Nombre",
    'website': "http://www.taller-mecanico.com",
    'category': 'Services',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/persona_view.xml',
        'views/cliente_view.xml',
        'views/menu_view.xml',
    ],
}
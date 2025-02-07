# __manifest__.py

{
    'name': 'Taller Mecánico',
    'version': '1.0',
    'summary': 'Gestión de taller mecánico: vehículos, reparaciones y mecánicos',
    'description': """
        Módulo de Odoo para gestionar un taller mecánico:
        - Gestión de clientes y vehículos
        - Registro de reparaciones
        - Gestión de mecánicos y líneas de reparación
        - Informes detallados
    """,
    'author': 'Tu Nombre o Grupo',
    'website': 'https://www.example.com',
    'category': 'Industries',
    'depends': ['base'],  # Dependencia de los módulos básicos de Odoo
    'data': [
        'security/ir.model.access.csv',
        'views/persona_view.xml',
        'views/mecanico_view.xml',
        'views/modelo_hijo2_views.xml',
        'views/otros_modelos_views.xml',
        'data/demo_data.xml',
        'reports/informe.xml',
    ],
    'demo': [
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

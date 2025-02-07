{
    'name': 'Gestión de Taller Mecánico',
    'version': '1.0',
    'summary': 'Gestión de taller mecánico: clientes, vehículos, reparaciones y mecánicos',
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
    'depends': ['base'],  # Dependencias necesarias para el módulo

    'data': [
    'security/ir.model.access.csv',

    # 📌 Primero se definen las acciones y vistas necesarias
    'views/cliente_action.xml',
    'views/cliente_views.xml',

    # 📌 Luego se carga el menú, que hace referencia a esas acciones
    'views/menu_view.xml',

    # 📌 Otras vistas
    'views/persona_view.xml',
    'views/mecanico_view.xml',
    'views/vehiculo_form_view.xml',
    'views/reparacion_views.xml',
    'views/lineareparacion_views.xml',
    'views/concepto_views.xml',

    # 📌 Datos de demostración
    'data/demo_data.xml',

    # 📌 Informes
    'reports/informe.xml',
    ],

    'demo': [
        'data/demo_data.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}

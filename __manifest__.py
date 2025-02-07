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
    

    # 📌 Luego se carga el menú, que hace referencia a esas acciones
   

    # 📌 Otras vistas
    'views/persona_view.xml',
<<<<<<< HEAD


=======
    'views/mecanico_view.xml',
    'views/cliente_views.xml',
    'views/vehiculo_form_view.xml',
    'views/reparacion_views.xml',
    'views/lineareparacion_views.xml',
    'views/concepto_views.xml',
>>>>>>> 92a9b2bf9076f9de18b1f303bc6b45a93327ba9d

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

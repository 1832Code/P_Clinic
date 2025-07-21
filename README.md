# Simulador de Sistema de Colas para Hospital

## Descripción
Este proyecto es un sistema web desarrollado en Python que simula y gestiona la atención de pacientes en un hospital, permitiendo la administración de áreas, doctores, pacientes y atenciones, así como la visualización de reportes y estadísticas en tiempo real.

## Características
- Registro e inicio de sesión de usuarios con seguridad.
- Gestión de áreas, doctores, pacientes y atenciones desde la web.
- Formularios profesionales y validaciones.
- Reportes y gráficos generados dinámicamente (matplotlib).
- Configuración de usuario y cambio de contraseña.
- Interfaz moderna y responsiva con Bootstrap.
- Persistencia de datos con MySQL.

## Paradigmas de Programación Aplicados
- **Orientado a Objetos:** Clases `Paciente`, `Doctor`, `Area` para modelar entidades.
- **Funcional:** Uso de funciones para reportes, filtros, conteos y generación de gráficos.
- **Estructurado:** Flujo principal de la aplicación, rutas, validaciones y menús.

## Instalación
1. Clona el repositorio o descarga el código.
2. Instala las dependencias:
   ```bash
   pip install flask mysql-connector-python matplotlib werkzeug
   ```
3. Crea la base de datos MySQL y las tablas necesarias (ver `db_config.py` para el script SQL).
4. Configura tu usuario y contraseña de MySQL en `db_config.py`.
5. Ejecuta la aplicación:
   ```bash
   python app.py
   ```
6. Accede a [http://127.0.0.1:5000/](http://127.0.0.1:5000/) en tu navegador.

## Estructura del Proyecto
```
PROYECTO/
│
├── app.py              # Lógica principal y rutas Flask
├── db_utils.py         # Funciones CRUD para la base de datos
├── db_config.py        # Configuración de conexión a MySQL
├── models.py           # Clases orientadas a objetos
├── templates/          # Plantillas HTML (Bootstrap + Jinja2)
├── static/             # (Opcional) Archivos estáticos
├── reports.py          # (Opcional) Lógica de reportes
├── simulation.py       # (Opcional) Lógica de simulación
├── utils.py            # Funciones utilitarias
└── README.md           # Este archivo
```

## Ejemplo de Uso
1. Regístrate como usuario.
2. Crea áreas, doctores y pacientes desde la web.
3. Registra atenciones y visualiza reportes y gráficos en la sección "Reportes".
4. Configura tu perfil y cambia tu contraseña desde el menú de usuario.

## Capturas de Pantalla
- Página principal y login
- Gestión de entidades
- Reportes y gráficos

## Autores
- Darwin Joel

## Licencia
Este proyecto es solo para fines educativos. 
import mysql.connector

# Configuración de la conexión
DB_CONFIG = {
    'user': 'root',         # Cambia por tu usuario de MySQL
    'password': 'karjoel', # Cambia por tu contraseña de MySQL
    'host': 'localhost',
    'database': 'hospital_simulador',
    'raise_on_warnings': True
}

# Recuerda crear la tabla usuarios en tu base de datos MySQL:
# CREATE TABLE IF NOT EXISTS usuarios (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     nombre VARCHAR(100) NOT NULL,
#     email VARCHAR(100) NOT NULL UNIQUE,
#     password_hash VARCHAR(255) NOT NULL
# );

def get_connection():
    """Devuelve una conexión activa a la base de datos MySQL."""
    return mysql.connector.connect(**DB_CONFIG) 
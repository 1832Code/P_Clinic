import mysql.connector

# Configuración de la conexión
DB_CONFIG = {
    'user': 'root',         
    'password': 'karjoel', 
    'host': 'localhost',
    'database': 'hospital_simulador',
    'raise_on_warnings': True
}

def get_connection():
    """Devuelve una conexión activa a la base de datos MySQL."""
    return mysql.connector.connect(**DB_CONFIG) 
import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Carga las variables definidas en el archivo .env
load_dotenv()

def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', ''),
            database=os.getenv('DB_NAME', 'salud_integral')
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

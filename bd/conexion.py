import mysql.connector

# Establecemos Coneccion con nuestro host
# Conn empieza la coneccion


def conecciones():
    db = mysql.connector.connect(host="localhost", user="root", password="admin123", db="hotel_ad", port=3306)
    return db
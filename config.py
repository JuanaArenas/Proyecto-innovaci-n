import oracledb  # pip install cx_Oracle
import os

# Datos de conexión a Oracle Cloud
cdx=oracledb.connect(
    user ="admin",
    password ="1234",
    dsn ="localhost:1521/producto"
    )


# Crear una conexión a Oracle
cursor = cdx.cursor()
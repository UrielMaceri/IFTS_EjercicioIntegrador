import pyodbc

def get_connection():
    return pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=D4RKN16H7-PC\LOCALTEST;"
        "DATABASE=EjercicioIntegrador;"
        "Trusted_Connection=yes;"
    )
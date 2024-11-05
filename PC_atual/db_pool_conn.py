import pyodbc

def get_db_connection():
    connection_string = (
        'DRIVER={SQL Server Native Client 11.0};'
        'SERVER=192.168.0.2;'
        'DATABASE=sapiens;'
        'UID=sapiens;'
        'PWD=sapiens;'
        'TrustServerCertificate=yes;'
    )
    conn = pyodbc.connect(connection_string)
    return conn
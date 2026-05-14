import pyodbc

def get_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 13 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=ExpenseDB;"
        "Trusted_Connection=yes;"
    )
    return conn
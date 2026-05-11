import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='natnael',
        password=''
    )
    with connection.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS Inventory")
    print("Database 'Inventory' created successfully.")
    connection.close()
except Exception as e:
    print(f"Error: {e}")

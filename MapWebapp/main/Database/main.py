import pyodbc

connection_string = 'DRIVER={SQL Server};SERVER=.;DATABASE=KARTA'
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

def eventList(UserId):
    connection_string = 'DRIVER={SQL Server};SERVER=.;DATABASE=KARTA'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    cursor.execute(f'GetAllEventsByUserId {UserId}')
    result = cursor.fetchall()

    connection.commit()
    connection.close()

    return result
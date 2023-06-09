import pyodbc

'''connection_string = 'DRIVER={SQL Server};SERVER=.;DATABASE=KARTA'
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()'''

def eventList(UserId):
    connection_string = 'DRIVER={SQL Server};SERVER=.;DATABASE=KARTA'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    cursor.execute(f"GetAllEventsByUserId {UserId}")
    result = cursor.fetchall()

    connection.commit()
    connection.close()

    return result

def createEvent(UserId, Name, Location, Description):
    connection_string = 'DRIVER={SQL Server};SERVER=.;DATABASE=KARTA'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    cursor.execute(f"CreateEvent {UserId}, '{Name}', '{Location}', '{Description}', 0")

    connection.commit()
    connection.close()

def deleteEvent(EventId):
    connection_string = 'DRIVER={SQL Server};SERVER=.;DATABASE=KARTA'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    cursor.execute(f"DeleteEventById {EventId}")

    connection.commit()
    connection.close()


def createUser(nickname, password):
    connection_string = 'DRIVER={SQL Server};SERVER=.;DATABASE=KARTA'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    cursor.execute(f"createUser '{nickname}', '{password}', 0")

    connection.commit()
    connection.close()

def loginUser(nickname, password):
    connection_string = 'DRIVER={SQL Server};SERVER=.;DATABASE=KARTA'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    cursor.execute(f"GetUserByNicknamePassword '{nickname}', '{password}'")
    result = cursor.fetchall()

    connection.commit()
    connection.close()

    return result
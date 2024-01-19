import sqlite3

def insertVariableIntoTable(first_name, last_name, phone, email):
    try:
        sqliteConnection = sqlite3.connect('py4bio_meeting_2023.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """insert into alt_speaker(first_name,last_name,phone,email) 
                                values(?,?,?,?);"""

        data_tuple = (first_name,last_name,phone,email)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into speaker table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

insertVariableIntoTable('Joe', 'Bonamassa',23987,'joe@blues.org')
insertVariableIntoTable('Carlos', 'Santana',77755,'carlos@blues.org')
insertVariableIntoTable('Linus', 'Torvalds',88888,'linus@.linux.org')

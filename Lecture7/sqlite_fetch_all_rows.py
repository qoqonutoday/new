import sqlite3

def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('py4bio_meeting_2023.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from alt_speaker"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("speaker_id: ", row[0])
            print("first_name: ", row[1]) 
            print("last_name: ", row[2])
            print("phone: ", row[3])
            print("email: ", row[4])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

readSqliteTable()

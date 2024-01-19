import sqlite3

def readLimitedRows(rowSize):
    try:
        sqliteConnection = sqlite3.connect('py4bio_meeting.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from session WHERE description LIKE \"%a%\""""
        cursor.execute(sqlite_select_query)
        print("Reading ", rowSize, " rows")
        records = cursor.fetchmany(rowSize)
        print("Printing each row \n")
        for row in records:
            print("name: ", row[0])
            print("speaker_id: ", row[1])
            print("description: ", row[2])
            print("start: ", row[3])
            print("duration: ", row[4])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

readLimitedRows(2)

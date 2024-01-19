import sqlite3

def readSingleRow(speaker_id):
    try:
        sqliteConnection = sqlite3.connect('py4bio_meeting_2023.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from alt_speaker where speaker_id = ?"""
        cursor.execute(sqlite_select_query, (speaker_id, ))
        print("Reading single row \n")
        record = cursor.fetchone()
        print("speaker_id: ", record[0])
        print("first_name: ", record[1])
        print("last_name: ", record[2])
        print("phone: ", record[3])
        print("email: ", record[4])
        print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

readSingleRow(1)

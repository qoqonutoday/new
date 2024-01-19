import sqlite3

def getSpeakerInfo(speaker_id):
    try:
        sqliteConnection = sqlite3.connect('py4bio_meeting_2023.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from alt_speaker where speaker_id = ?"""
        cursor.execute(sql_select_query, (speaker_id,))
        records = cursor.fetchall()
        print("Printing ID ", speaker_id)
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

getSpeakerInfo(2)

import sqlite3

def deleteMultipleRecords(speaker_idList):
    try:
        sqliteConnection = sqlite3.connect('py4bio_meeting.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_update_query = """DELETE from speaker where speaker_id = ?"""

        cursor.executemany(sqlite_update_query, speaker_idList)
        sqliteConnection.commit()
        print("Total", cursor.rowcount, "Records deleted successfully")
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete multiple records from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")

speaker_idsToDelete = [(9,),(10,)]
deleteMultipleRecords(speaker_idsToDelete)

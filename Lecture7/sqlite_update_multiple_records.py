import sqlite3

def updateMultipleRecords(recordList):
    try:
        sqliteConnection = sqlite3.connect('py4bio_meeting_2023.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_update_query = """Update alt_speaker set phone = ? where speaker_id = ?"""
        cursor.executemany(sqlite_update_query, recordList)
        sqliteConnection.commit()
        print("Total", cursor.rowcount, "Records updated successfully")
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update multiple records of sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

records_to_update = [ (12345, 4), (45678, 5), (98765, 6) ]
updateMultipleRecords(records_to_update)

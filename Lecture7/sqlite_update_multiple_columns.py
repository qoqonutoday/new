import sqlite3

def updateMultipleColumns(speaker_id, phone, email):
    try:
        sqliteConnection = sqlite3.connect('py4bio_meeting_2023.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_update_query = """Update alt_speaker set phone = ?, email = ? where speaker_id = ?"""
        columnValues = (phone, email, speaker_id)
        cursor.execute(sqlite_update_query, columnValues)
        sqliteConnection.commit()
        print("Multiple columns updated successfully")
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update multiple columns of sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")

updateMultipleColumns(5, 66666, 'vlad.dracula@gmail.com')

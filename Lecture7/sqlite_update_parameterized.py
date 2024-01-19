import sqlite3

def updateSqliteTable(speaker_id, phone):
    try:
        sqliteConnection = sqlite3.connect('py4bio_meeting_2023.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """Update alt_speaker set phone = ? where speaker_id = ?"""
        data = (phone, speaker_id)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        print("Record Updated successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The sqlite connection is closed")

updateSqliteTable(3, 75006)

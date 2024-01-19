import sqlite3

def deleteSqliteRecord(speaker_id):
    try:
        sqliteConnection = sqlite3.connect('py4bio_meeting_2023.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """DELETE from alt_speaker where speaker_id = ?"""
        cursor.execute(sql_update_query, (speaker_id, ))
        sqliteConnection.commit()
        print("Record deleted successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")

deleteSqliteRecord(5)

import sqlite3

try:
    sqliteConnection = sqlite3.connect('py4bio_meeting.db')
    cursor = sqliteConnection.cursor()
    print("Database created and successfully connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite database version is: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")

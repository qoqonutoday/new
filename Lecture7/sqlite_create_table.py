import sqlite3

try:
    sqliteConnection = sqlite3.connect('py4bio_meeting_2023.db')
    sqlite_create_table_query = '''CREATE TABLE `alt_speaker` (
 	                            `speaker_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	                            `first_name`	varchar ( 128 ) NOT NULL,
	                            `last_name`	varchar ( 128 ) NOT NULL,
	                            `phone`	int ( 10 ) NOT NULL,
	                            `email`	varchar ( 255 ) NOT NULL);'''

    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("sqlite connection is closed")

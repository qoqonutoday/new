import sqlite3

try:
    sqliteConnection = sqlite3.connect('py4bio_meeting_2023.db')
    sqlite_create_table_session = '''CREATE TABLE `alt_session` (
                                    `name`	varchar ( 60 ) NOT NULL,
                                    `speaker_id`	INTEGER NOT NULL UNIQUE,
                                    `description`	varchar ( 500 ) NOT NULL,
                                    `start`	datetime NOT NULL,
                                    `duration`	INTEGER NOT NULL,
                                    PRIMARY KEY(`name`)); '''

    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_session)
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("sqlite connection is closed")

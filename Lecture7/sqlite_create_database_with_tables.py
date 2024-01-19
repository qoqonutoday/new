import sqlite3

try:
    sqliteConnection = sqlite3.connect('py4bio_2022_meeting_V2.db')
    sqlite_create_table_speaker = '''CREATE TABLE `speaker` (
                                    `speaker_id`        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    `first_name`        varchar ( 128 ) NOT NULL,
                                    `last_name` varchar ( 128 ) NOT NULL,
                                    `phone`     int ( 10 ) NOT NULL,
                                    `email`     varchar ( 255 ) NOT NULL);'''


    sqlite_create_table_session = '''CREATE TABLE `session` (
                                    `name`	varchar ( 60 ) NOT NULL,
                                    `speaker_id`	INTEGER NOT NULL UNIQUE,
                                    `description`	varchar ( 500 ) NOT NULL,
                                    `start`	datetime NOT NULL,
                                    `duration`	INTEGER NOT NULL,
                                    PRIMARY KEY(`name`)); '''

    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_speaker)
    cursor.execute(sqlite_create_table_session)
    sqliteConnection.commit()
    print("SQLite tables 'speaker' and 'session' created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("sqlite connection is closed")

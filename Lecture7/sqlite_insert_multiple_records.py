import sqlite3

def insertMultipleRecords(recordList):
    try:
        sqliteConnection = sqlite3.connect('py4bio_meeting_2023.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_query = """insert into alt_speaker(first_name,last_name,phone,email)
                                values(?,?,?,?);"""

        cursor.executemany(sqlite_insert_query, recordList)
        sqliteConnection.commit()
        print("Total", cursor.rowcount, "Records inserted successfully into speaker table")
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

recordsToInsert = [('Jos','Vermeulen',55555,'jos@gmail.com'),
                   ('Chris','De Wilde',44444,'chris@gmail.com'),
                   ('Jonny','Winter',22222,'jonny@gmail.com')]

insertMultipleRecords(recordsToInsert)

import sqlite3

try:
    sqliteConnection = sqlite3.connect('py4bio_meeting_2023.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_speaker = """insert into alt_speaker(first_name,last_name,phone,email) 
                                values('Marie','Curie',987654,'mariec@science-heaven.be');"""

    count = cursor.execute(sqlite_insert_speaker)
    sqliteConnection.commit()
    print("Record inserted successfully into speaker table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")

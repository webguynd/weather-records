import sqlite3

DB_TABLE_SETUP = '''CREATE TABLE weather (
    id integer PRIMARY KEY,
    current_conditions TEXT NOT NULL,
    current_temperature integer NOT NULL,
    wind_speed integer NOT NULL,
    rainfall_hour integer NOT NULL,
    date string NOT NULL
);'''

def createDatabase():
    try:
        sqlCon = sqlite3.connect("wr.db")
        cursor = sqlCon.cursor()
    except sqlite3.Error as error:
        print("Error: ", error)
    finally:
        if(sqlCon):
            cursor.execute(DB_TABLE_SETUP)
            sqlCon.commit()
            print("Database created successfully. Exiting setup now")


print("Welcome to Weather Records setup!\n")
print("I will now create an SQLite database in this directory")
createDatabase()
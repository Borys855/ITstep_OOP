import sqlite3

connection = sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()

#cur.execute("CREATE TABLE first_table (nameTEXT);")
#cur.execute("DROP TABLE sqlite_master;")
#cur.execute("INSERT INTO first_table (name) VALUES ('igor');")
#cur.execute("SELECT rowid, name FROM first_table;")

#cur.execute("UPDATE first_table SET name='Marina' WHERE rowid=2;")

#cur.execute("UPDATE first_table SET name='Marina' WHERE rowid=2")
#cur.execute(





cur.execute("DROP TABLE first_table")
connection.commit()

print(connection)
print(cur)
connection.close()

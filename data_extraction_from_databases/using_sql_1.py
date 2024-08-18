import database_setup
import sqlite3

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

select_query = '''
SELECT Name, Marks, Section 
FROM student
WHERE Grade = 'A'
'''

cursor.execute(select_query)
result = cursor.fetchall()
print(result)

conn.close()
import sqlite3
conn = sqlite3.connect("my_database.db")
cursor =conn.cursor()
table_creation_query = '''
            CREATE TABLE IF NOT EXISTS Student (
                Student_Id INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                Section TEXT,
                Marks INTEGER,
                Grade TEXT
            );
            '''
cursor.execute(table_creation_query)
insert_query = '''
INSERT INTO Student (Student_Id, Name, Section, Marks, Grade) VALUES (6, 'Ross', 'A', 97, 'A')'''

cursor.execute(insert_query)
conn.commit()
conn.close()
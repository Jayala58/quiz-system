import sqlite3

conn = sqlite3.connect("quiz.db")
cursor = conn.cursor()

# Create questions table
cursor.execute('''
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct TEXT NOT NULL
)
''')

# Delete old questions if any
cursor.execute("DELETE FROM questions")

# Insert 10 Python + SQL questions
questions = [
    ("Which of the following is used to define a function in Python?", "func", "def", "function", "define", "B"),
    ("What is the output of: len([1, 2, 3])?", "2", "3", "4", "Error", "B"),
    ("Which SQL keyword is used to extract data from a database?", "SELECT", "EXTRACT", "GET", "FETCH", "A"),
    ("What is the correct file extension for Python files?", ".pt", ".pyt", ".py", ".python", "C"),
    ("In SQL, which command is used to remove all records from a table?", "DELETE", "DROP", "CLEAR", "TRUNCATE", "D"),
    ("Which operator is used for exponentiation in Python?", "^", "**", "//", "exp()", "B"),
    ("Which clause is used to filter records in SQL?", "ORDER BY", "WHERE", "GROUP BY", "HAVING", "B"),
    ("What does the 'fetchall()' method return in Python's sqlite3?", "One row", "All rows", "Only column names", "None", "B"),
    ("Which data type is used to store a sequence of characters in Python?", "int", "str", "char", "text", "B"),
    ("Which SQL statement is used to insert new data into a table?", "ADD", "APPEND", "INSERT INTO", "PUT", "C"),
]
cursor.executemany('''
INSERT INTO questions (question, option_a, option_b, option_c, option_d, correct)
VALUES (?, ?, ?, ?, ?, ?)''', questions)

# Create leaderboard table
cursor.execute('''
CREATE TABLE IF NOT EXISTS leaderboard (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    score INTEGER NOT NULL,
    date_taken TEXT NOT NULL
)
''')

conn.commit()
conn.close()
print("✅Successfully created database with 10 Python + SQL questions.")

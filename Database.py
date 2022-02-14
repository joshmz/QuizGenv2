# The use of this class is to initiate my database
# Keeping database initiator separate


import sqlite3

conn = sqlite3.connect('quizDB.db')
cursor = conn.cursor()


#  CREATE TABLES

#   MODULES TABLE
module_table = """CREATE TABLE IF NOT EXISTS modules (
                    module_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    moduleName TEXT, 
                    moduleDesc TEXT)"""

#   QUESTIONS TABLE
question_table = """CREATE TABLE IF NOT EXISTS questions (
                    question_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    module TEXT,
                    qType INT,
                    question TEXT,
                    answer TEXT,
                    options TEXT,
                    mark TEXT,
                    FOREIGN KEY(module) REFERENCES modules (moduleName))"""

#   RESULTS TABLE
results_table = """CREATE TABLE IF NOT EXISTS results (
                    result_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    module TEXT,
                    score INTEGER,
                    date TEXT)"""

cursor.execute(module_table)
cursor.execute(question_table)
cursor.execute(results_table)

#   GET MODULE NAMES
cursor.execute("SELECT moduleName FROM modules")
module_name_list = cursor.fetchall()

#   GET DESCRIPTIONS
cursor.execute("SELECT moduleDesc FROM modules")
module_desc_list = cursor.fetchall()

conn.commit()


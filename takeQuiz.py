import Database as db
import random

questions_list = []
answer_list = []
options_list = []

def fetch_questions(module):
    m = module.strip("(',)")

    #   FETCH QUESTIONS FROM DATABASE IN CHOSEN MODULES
    db.cursor.execute(f"SELECT * FROM questions WHERE module = '{m}'")
    question_data = db.cursor.fetchall()
    db.cursor.execute(f"SELECT question FROM questions WHERE module = '{m}'")
    questions = db.cursor.fetchall()
    db.cursor.execute(f"SELECT answer FROM questions WHERE module = '{m}'")
    answer = db.cursor.fetchall()
    db.cursor.execute(f"SELECT options FROM questions WHERE module = '{m}'")
    options = db.cursor.fetchall()

    #   GET A LIST OF RANDOM QUESTION IDs
    random_IDs = random.sample(range(1,len(question_data)),5)

    for i in (random_IDs):
        
        questions_list.append(questions[i])
        answer_list.append(answer[i])
        options_list.append(options[i])

def update_results(module,mark,date):
    m= module.strip("(',)")
    result = [
        m,
        mark,
        date
    ]
    db.cursor.execute(f"INSERT INTO results (module,score,date) VALUES (?,?,?)",result)
    db.conn.commit()

    


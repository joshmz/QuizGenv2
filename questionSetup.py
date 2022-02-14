import Database as db

question_types = [
    "Multiple Choice",
    "True False",
    "Best Chance"
]

class Question:
    def __init__(self,qs_type,qs_module,question,answer,options):
        self.qs_type = qs_type
        self.qs_module = qs_module
        self.question = question
        self.answer = answer
        self.options = options
    
    def insert_data(self):
        question = [
            self.qs_module,
            self.qs_type,
            self.question,
            self.answer,
            self.options
        ]

        db.cursor.execute("INSERT INTO questions (module, qType, question, answer, options) VALUES (?,?,?,?,?)",question)
        db.conn.commit()

class BestMatch(Question):
    def __init__(self,qs_type,qs_module,terms,definitions):
        super(BestMatch,self).__init__(qs_type,qs_module,None,None,None)
        self.terms = terms
        self.definitions = definitions
    
    def insert_data(self):
        question = [
            self.qs_module,
            self.qs_type,
            self.terms,
            self.definitions
        ]
        db.cursor.execute("INSERT INTO questions (module, qType, question, answer) VALUES (?,?,?,?)",question)
        db.conn.commit()

def make_question(type,mod,qs,ans,opt):
    mod = mod.strip("('),")
    qs = ''.join(qs)
    ans = ''.join(ans)
    question_instance = Question(type, mod, qs, ans, opt)
    question_instance.insert_data()

def make_bm_question(type,mod,terms,defs):
    mod = mod.strip("('),")
    terms = ''.join(terms)
    defs = ''.join(defs)
    question_instance = BestMatch(type,mod,terms,defs)
    question_instance.insert_data()
from tkinter import *
import Database as db
import moduleSetup as mdl
import questionSetup as qs
import takeQuiz as tq
import random

root = Tk()
root.title("QUIZ GENERATOR")
root.geometry("400x200")

class Elder:
    def __init__(self, master,title):
        self.master = master
        self.title = title

        #   TITLE
        self.title = Label(self.master, text=self.title, font=("Helvetica", 16))
        self.title.grid(row=0,column=0,columnspan=2, padx="100",pady="10")

        def make_module(win):
            new_win = Toplevel()
            new_win.geometry("400x200")
            title = Label(new_win,text=win,font=("Helvetica", 16))
            title.grid(row=0,column=0,columnspan=2, padx="130",pady="10")

            #   BACK TO MAIN MENU
            back_button = Button(new_win, text="BACK", command= lambda: new_win.destroy())
            back_button.grid(row=4,column=0,columnspan=2,ipady=5)

            module_entries = []

            def get_inputs():
                module_data = []
                for entry in module_entries:
                    module_data.append(entry.get())
                
                #   SEPERATE NAME AND DESC FROM ARRAY
                module_name = module_data[0]
                module_desc = module_data[1]

                if module_name in db.module_name_list:
                    print("Already a module with that name")
                else:
                    mdl.create_module(module_name,module_desc)


                new_win.destroy() # DESTROY WINDOW WHEN MODULE IS REGISTERED

            #   MAKE TWO ENTRY BOXES
            for x in range (2):
                entry_box = Entry(new_win)
                entry_box.grid(row=1+x,column=0, columnspan=2)
                module_entries.append(entry_box)

            reg_module_button = Button(new_win, text="REGISTER MODULE", command=get_inputs)
            reg_module_button.grid(row=3,column=0,columnspan=2,ipady=5)

        def make_question(win):
            new_win = Toplevel()
            new_win.geometry("400x150")
            title = Label(new_win,text=win,font=("Helvetica", 16))
            title.grid(row=0,column=0,columnspan=2, padx="110",pady="10")

            #   BACK TO MAIN MENU
            back_button = Button(new_win, text="BACK", command= lambda: new_win.destroy())
            back_button.grid(row=11,column=0,columnspan=2,ipady=5)

            def selected(event):
                new_win = Toplevel()
                new_win.geometry("400x100")
                title = Label(new_win,text=win,font=("Helvetica", 16))
                title.grid(row=0,column=0,columnspan=2, padx="110",pady="10")

                question_module = StringVar()
                question_module.set("CHOOSE MODULE")

                #   DISPLAY MODULE CHOUCE
                qs_module_optionmenu = OptionMenu(new_win, question_module, *db.module_name_list)
                qs_module_label = Label(new_win,text="Choose Module").grid(row=2,column=0,columnspan=1,ipady=5)
                qs_module_optionmenu.grid(row=2,column=1,columnspan=2,ipady=5)

                #   BACK TO MAIN MENU
                back_button = Button(new_win, text="BACK", command= lambda: new_win.destroy())
                back_button.grid(row=15,column=0,columnspan=2,ipady=5)

                #   MULTIPLE CHOICE
                if question_type.get() == qs.question_types[0]:
                    new_win.geometry("400x400")
                    false_ans_entries = []
                    #   ENTER QUESTION
                    qs_entry = Entry(new_win,width=25)
                    qs_entry_label = Label(new_win,text="Enter Question").grid(row=3,column=0,columnspan=1,ipady=5)
                    qs_entry.grid(row=3,column=1,columnspan=1,ipady=5)
            
                    #   ENTRY ANSWER
                    qs_answer_entry = Entry(new_win,width=25)
                    qs_answer_label = Label(new_win,text="Enter Answer").grid(row=4,column=0,columnspan=1,ipady=5)
                    qs_answer_entry.grid(row=4,column=1,columnspan=1,ipady=5)

                    def get_inputs():
                        false_answers_data = [qs_answer_entry.get()]
                        for false_answers in false_ans_entries:
                            false_answers_data.append(false_answers.get())

                        #   FORMAT LIST INTO STRING SO IT CAN BE STORED IN DB
                        #   EACH ANSWER IS SEPERATED BY A ;
                        false_ans_string = ';'.join(false_answers_data)
                        qs.make_question(0, question_module.get(), qs_entry.get(), qs_answer_entry.get(), false_ans_string)    

                        new_win.destroy() # DESTROY WINDOW WHEN MODULE IS REGISTERED

                    for x in range (4):
                        false_ans_label = Label(new_win,text=f'False Answer {x+1}:').grid(row=5+x,column=0,columnspan=1,ipady=5)
                        entry_box = Entry(new_win,width=25)
                        entry_box.grid(row=5+x,column= 1, columnspan=1,ipady=5)
                        false_ans_entries.append(entry_box)

                        reg_question_button = Button(new_win, text="REGISTER QUESTION", command=get_inputs)
                        reg_question_button.grid(row=10,column=0,columnspan=2,ipady=5)

                #   TRUE FALSE
                elif question_type.get() == qs.question_types[1]:
                    new_win.geometry("400x300")
                    #   RETURN 1 IF TRUE; 0 IF FALSE
                    ans = IntVar()

                    def define_answers():
                        if ans.get() == 0:
                            statement_true = "False"
                        elif ans.get() == 1:
                            statement_true = "True"

                        qs.make_question(1, question_module.get(), qs_entry.get(), statement_true, "True;False")
                        new_win.destroy()
                        
                    #   ENTER QUESTION
                    qs_entry = Entry(new_win,width=25)
                    qs_entry_label = Label(new_win,text="Enter Question").grid(row=3,column=0,columnspan=1,ipady=5)
                    qs_entry.grid(row=3,column=1,columnspan=1,ipady=5)
            
                    #   ENTRY ANSWER
                    qs_answer_entry = Checkbutton(new_win,variable=ans)
                    qs_answer_label = Label(new_win,text="Tick If Statement Is True: ").grid(row=4,column=0,columnspan=1,ipady=5)
                    qs_answer_entry.grid(row=4,column=1,columnspan=1,ipady=5)

                    #   REGISTER QUESTION BUTTON
                    reg_question_button = Button(new_win, text="REGISTER QUESTION", command=define_answers)
                    reg_question_button.grid(row=10,column=0,columnspan=2,ipady=5)

                #   BEST MATCH
                else:
                    new_win.geometry("400x500")

                    terms = []

                    def get_inputs():
                        term_data = []
                        for term in terms:
                            term_data.append(term.get())
                        
                        #   SEPERATE TERMS AND DEFINITIONS INTO THEIR OWN LISTS
                        only_terms = term_data[::2]
                        only_definitions = term_data[1::2]

                        #   FORMAT LIST SO IT CAN GOTO DATABASE
                        terms_string = ';'.join(only_terms)
                        def_string = ';'.join(only_definitions)

                        qs.make_bm_question(2, question_module.get(), terms_string, def_string)
                        new_win.destroy() # DESTROY WINDOW WHEN MODULE IS REGISTERED

                    for x in range (8):
                        entry_box = Entry(new_win,width=25)
                        entry_box.grid(row=5+x,column= 1, columnspan=1,ipady=5)
                        terms.append(entry_box)
                    
                    #   LABELS FOR TERM AND DEFINITIONS ALTERNATING
                    Label(new_win,text="Term 1: ").grid(row=5,column=0,columnspan=1,ipady=5)
                    Label(new_win,text="Definition 1: ").grid(row=6,column=0,columnspan=1,ipady=5)
                    Label(new_win,text="Term 2: ").grid(row=7,column=0,columnspan=1,ipady=5)
                    Label(new_win,text="Definition 2: ").grid(row=8,column=0,columnspan=1,ipady=5)
                    Label(new_win,text="Term 3: ").grid(row=9,column=0,columnspan=1,ipady=5)
                    Label(new_win,text="Definition 3: ").grid(row=10,column=0,columnspan=1,ipady=5)
                    Label(new_win,text="Term 4: ").grid(row=11,column=0,columnspan=1,ipady=5)
                    Label(new_win,text="Definition 4: ").grid(row=12,column=0,columnspan=1,ipady=5)

                    reg_question_button = Button(new_win, text="REGISTER QUESTION", command=get_inputs)
                    reg_question_button.grid(row=14,column=0,columnspan=2,ipady=5)


            question_type = StringVar()
            question_type.set("CHOOSE TYPE")

            #   DISPLAY TYPE CHOICE
            qs_type_optionmenu = OptionMenu((new_win), question_type, *qs.question_types, command=selected)
            qs_type_label = Label(new_win,text="Choose Type").grid(row=1,column=0,columnspan=1,ipady=5)
            qs_type_optionmenu.grid(row=1,column=1,columnspan=2,ipady=5)

        def view_modules(win):
            new_win = Toplevel()
            new_win.geometry("400x200")
            title = Label(new_win,text=win,font=("Helvetica", 16))
            title.grid(row=0,column=0,columnspan=3, padx="110",pady="10")

            chosen_module = StringVar()
            chosen_module.set("CHOOSE MODULE")

            def update_module(name,desc):
                i = chosen_module.get()
                i.strip("(',)")
                #print(name,desc)
                db.cursor.execute(f"UPDATE modules SET moduleName = {name}, moduleDesc = {desc} WHERE moduleName = '{i}'")

            def selected(event):
                module = chosen_module.get()
                m = module.strip("(',)")
                print(m)
                db.cursor.execute(f"SELECT * FROM modules WHERE moduleName = '{m}'")
                selected_module = db.cursor.fetchall()
                db.cursor.execute(f"SELECT moduleDesc FROM modules WHERE moduleName = '{m}'")
                selected_module_desc = db.cursor.fetchall()
                Label(new_win,text="Description").grid(row=3,column=1)
                Label(new_win,text=selected_module_desc,bg="grey",width=10).grid(row=4,column=1)
                Label(new_win,text="Module Name: ").grid(row=5,column=0)
                Label(new_win,text="Module Desc: ").grid(row=6,column=0)
                module_name = Entry(new_win,width=25)
                module_name.grid(row=5,column=1)
                module_des = Entry(new_win,width=25)
                module_des.grid(row=6,column=1)

                upd_module= Button(new_win,text="UPDATE MODULE", command= lambda: update_module(module_name.get(),module_des.get()))
                upd_module.grid(row=7,column=1)



            module_title = Label(new_win,text="Module")
            module_title.grid(row=1,column=1)
            module_dropdown = OptionMenu(new_win, chosen_module, *db.module_name_list, command = selected)
            module_dropdown.grid(row=2,column=1)


        def view_questions(win):
            pass

        #   MAKE NEW WINDOW FOR ADMIN TOOLS
        def create_new_win(win):

            user_answers = []

            new_win = Toplevel()
            new_win.geometry("400x250")
            title = Label(new_win,text=win,font=("Helvetica", 16))
            title.grid(row=0,column=0,columnspan=2, padx="130",pady="10")

            #   BACK TO MAIN MENU
            back_button = Button(new_win, text="BACK", command= lambda: new_win.destroy())
            back_button.grid(row=5,column=0,columnspan=2,ipady=5)

            def make_quiz(module):
                tq.fetch_questions(module)
                start_quiz()

            def start_quiz():
                new_win = Toplevel()
                new_win.geometry("400x200")

                q1 = Frame(new_win)
                q2 = Frame(new_win)
                q3 = Frame(new_win)
                q4 = Frame(new_win)
                q5 = Frame(new_win)
                show_answers = Frame(new_win)

                def swap(frame):
                    frame.tkraise()

                for frame in (q1,q2,q3,q4,q5,show_answers):
                    frame.grid(row=0,column=0,sticky="news")
                

                def create_question(screen,question,next_screen,last_screen):
                    question_label = Label(screen,text=tq.questions_list[question],font=("Helvetica", 14))
                    question_label.grid(row=1,column=0,columnspan=2)

                    option_string = ''.join(tq.options_list[question])
                    seperate_options = option_string.split(";")
                    random.shuffle(seperate_options)

                    if '' in seperate_options:
                        seperate_options.remove('')

                    #   ADDS TO USER ANSWERS
                    def add_to_answers(option):
                        if len(user_answers) != 5:
                            user_answers.append(option)
                            swap(next_screen)
                        confirm_button = Button(show_answers,text="REGISTER ANSWERS",command=lambda: reference_answer(user_answers))
                        x=1
                        for i in user_answers:
                            Label(show_answers, text=i).grid(row=x,column=1)
                            x+=1
                        confirm_button.grid(row=6,column=1)
                    
                    def reference_answer(answers):
                        correct = 0
                        print(tq.answer_list)
                        print(answers)
                        for x in range(5):
                            if answers[x] in tq.answer_list[x]:
                                correct+=1
                        tq.update_results(chosen_module.get(), correct, enter_name.get())                                   
                        

                    #   CREATE DIFFERENT BUTTONS DEPENDING ON TYPE OF QUESTION
                    
                    #   TRUE FALSE
                    if len(seperate_options) == 2:
                        true_button = Button(screen, text="True", command = lambda: add_to_answers("True"))
                        true_button.grid(row=2,column=0)
                        false_button = Button(screen, text="False", command = lambda: add_to_answers("False"))
                        false_button.grid(row=3,column=0)
                    
                    #   MULTIPLE CHOICE
                    else:
                        option_1 = Button(screen, text=seperate_options[0], command = lambda: add_to_answers(seperate_options[0]))
                        option_1.grid(row=2,column=0)
                        option_2 = Button(screen, text=seperate_options[1], command = lambda: add_to_answers(seperate_options[1]))
                        option_2.grid(row=3,column=0)
                        option_3 = Button(screen, text=seperate_options[2], command = lambda: add_to_answers(seperate_options[2]))
                        option_3.grid(row=4,column=0)
                        option_4 = Button(screen, text=seperate_options[3], command = lambda: add_to_answers(seperate_options[3]))
                        option_4.grid(row=5,column=0)

                    next_question = Button(screen,text="NEXT QUESTION",command = lambda: swap(next_screen))
                    next_question.grid(row=6,column=1)

                #   CREATE A DIFFERENT FRAME FOR EACH QUESTION
                create_question(q1,0,q2,q1)
                create_question(q2,1,q3,q1)
                create_question(q3,2,q4,q2)
                create_question(q4,3,q5,q3)
                create_question(q5,4,show_answers,q4)

                x=1
                for i in tq.questions_list:
                    Label(show_answers,text=i).grid(row=x,column=0)
                    x+=1

                Label(show_answers,text="Confirm Answers").grid(row=10,column=0,columnspan=2)

                q1.tkraise()

            #   TAKING QUIZ
            if "QUIZ" in win:
                chosen_module = StringVar()
                chosen_module.set("CHOOSE MODULE")
                choose_module_dropdown = OptionMenu(new_win, chosen_module, *db.module_name_list)
                choose_module_dropdown.grid(row=1,column=0,columnspan=2)

                enter_name = Entry(new_win,width=25)
                enter_name_label = Label(new_win,text="Enter Name").grid(row=2,column=0,columnspan=1)
                enter_name.grid(row=2,column=1)


                start_quiz_button = Button(new_win,text="START QUIZ",command= lambda: make_quiz(chosen_module.get()))
                start_quiz_button.grid(row=3, column=0,columnspan=2)
            # ADMIN TOOLS
            elif "ADMIN" in win:
                make_module_button = Button(new_win, text="MAKE MODULE", command= lambda: make_module("MAKE MODULE"))
                make_module_button.grid(row=1,column=0,columnspan=2,ipady=5)

                view_modulse_button = Button(new_win, text= 'EDIT MODULES', command= lambda: view_modules("VIEW MODULES"))
                view_modulse_button.grid(row=2,column=0,columnspan=2,ipady=5)

                make_question_button = Button(new_win, text="MAKE QUESTION", command= lambda: make_question("MAKE QUESTION"))
                make_question_button.grid(row=3,column=0,columnspan=2,ipady=5)

                view_questions_button = Button(new_win, text= 'VIEW QUESTIONS')
                view_questions_button.grid(row=4,column=0,columnspan=2,ipady=5)

        #   TAKE QUIZ BUTTON
        take_quiz_button = Button(self.master, text="TAKE QUIZ",command= lambda: create_new_win("TAKE QUIZ"))
        take_quiz_button.grid(row=1,column=0,columnspan=2,ipady=5)

        #   ADMIN TOOLS BUTTON
        admin_button = Button(self.master, text="ADMIN TOOLS",command= lambda: create_new_win("ADMIN TOOLS"))
        admin_button.grid(row=2,column=0,columnspan=2,ipady=5)

        #   EXIT BUTTON
        exit_button = Button(self.master, text="EXIT",command= lambda:exit())
        exit_button.grid(row=3,column=0,columnspan=2,ipady=5)
    
    #   REMOVES ALL ITEMS FROM THE SCREEN
    def remove_all_widgets(self):
        for widget in self.master.winfo_children():
            widget.destroy()

main_menu = Elder(root,"QUIZ GENERATOR")


root.mainloop()

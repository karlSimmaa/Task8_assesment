"""Customizable quiz python code for any subject, with a database to store questions and answers.
14/05/26 by KARL"""
import sqlite3

DB = 'quiz.db'

#functions
def initialize_data():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECt id, questions, answers FROM questions")
    rows = cursor.fetchall()
    ids = [row[0] for row in rows]  
    question = [row[1] for row in rows]
    answer = [row[2] for row in rows]
    return ids, question, answer

def check_question():
    ids, question, answer = initialize_data()
    if len(ids) > 0:
        print("There are questions in the database")
    else:
        print("Add questions to the database")

#start the quiz

def display_answer():
    question = initialize_data()[1]
    answer = initialize_data()[2]
    print(answer)

    for ques, ans in zip(question, answer):
        user_answer = input(f"{ques}: ")
        print(ans)
        if int(user_answer) == ans:
            print("Correct")
        else:
            print("Wrong")
        print(ans)
display_answer()
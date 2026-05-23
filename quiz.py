"""Customizable quiz python code for any subject, with a database to store questions and answers.
14/05/26 by KARLx"""
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


def add_question():
    added_question = initialize_data()[1]
    added_answer = initialize_data([2])

    while True:
        while True:
            question_input = input("Enter question: ").strip()
            if len(question_input) < 0:
                print("That's invalid, please enter a proper question ")
            else:
                added_question.append(question_input)
                break
        while True:
            answer_input = input(f"Enter Answer for {added_question[-1]}:==>: ").strip()
            if answer_input == None:
                print("Please Enter the Answer!")
            else:
                added_answer.append(answer_input)
                confirmation = input("Do you wan't to continue? y/n").lower
                if confirmation == 'y':
                    continue
                elif confirmation == 'n':
                    break
    return added_question, added_answer
    







def delete_question():


def view_all_question():
    all_q = initialize_data()[1]
    print(all_q)

    while True:
        user = input("add_question? y/n: ").strip().lower()
        if user == 'n':
            return 
        elif user == 'y':
            add_question()  
            return 
        else:
            print("Invalid input. Please enter 'y' or 'n'.")









#========Main menu========#
def main_menu():




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
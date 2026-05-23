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
    ids, added_question, added_answer = initialize_data()

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    while True:
        while True:
            question_input = input("Enter question: ").strip()
            if len(question_input) <= 0:
                print("That's invalid, please enter a proper question ")
            else:
                added_question.append(question_input)
                break
        while True:
            answer_input = input(f"Enter Answer for {added_question[-1]}:==>: ").strip()
            if len(answer_input) <= 0: 
                print("Please Enter the Answer!")
            else:
                added_answer.append(answer_input)

                cursor.execute("INSERT INTO questions (questions, answers) VALUES (?, ?)", 
                               (question_input, answer_input))
                conn.commit()
                print("Successfully saved to database!")
                break
        confirmation = input("Do you want to continue? y/n: ").strip().lower()
        if confirmation == 'n':
            break
    conn.close()
    
    return added_question, added_answer

    







def delete_question():
    ids, questions, answers = initialize_data()
    
    if len(ids) <= 0:
        print("There are no questions in the database to delete.")
        return
    for i in range(len(ids)):
        print(f"ID: {ids[i]} / Question: {questions[i]}")

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    
    while True:
        try:
            delete_id = int(input("Enter the id of the question you want to delete: "))
            if delete_id in ids:
                cursor.execute("DELETE FROM questions WHERE id = ?", (delete_id,))
                conn.commit()
                print(f"Question with id {delete_id} successfully deleted.")
                break
            else:
                print("That id does not exist. Please pick an id from the list.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the id.")
            
    conn.close()



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
            
#test
view_all_question()







#========Main menu========#



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
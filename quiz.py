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
    print("BEWARE This is CASE SENSITIVE!!")
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
            main_menu()
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
    user = input("Continue? y/n").lower().strip()
    if user == "y":
        delete_question()
    elif user == "n":
        main_menu()
        



def view_all_question():
    all_q = initialize_data()[1]
    print(all_q)

    while True:
        user = input("add_question? y/n: ").strip().lower()
        if user == 'n':
            main_menu()
            return 
        elif user == 'y':
            add_question()  
            return 
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            
#start the quiz

def quiz():
    question = initialize_data()[1]
    answer = initialize_data()[2]

    for ques, ans in zip(question, answer):
        user_answer = input(f"{ques}: ")
        print(ans)
        if (user_answer) == ans:
            print("Correct")
        else:
            print(f"Wrong it's {ans}")
    user = input("\nRestart Quiz or Main Menu? y/n").lower().strip()
    if user == "y":
        quiz()
    elif user == "n":
        main_menu()
    else:
        print("\nInvalid! Please Enter Correct Letter")


def main_menu():
    print("""Main Menu
          1. Take Quiz
          2. Add Question
          3. Delete Question
          5. View All Question
          4. Exit""")
    
    user_input = int(input("Enter number: "))
    if user_input == 1:
        print("\nQuiz starting: ")
        quiz()
    elif user_input == 2:
        add_question()
    elif user_input == 3:
        delete_question()
    elif user_input == 4:
        print("Thank you for plaing")
    elif user_input == 5:
        view_all_question()
    else:
        print("Invalid Number!!")
main_menu()
"""Customizable quiz python code for any subject, with a database to store questions and answers.
14/05/26 by KARLx"""
import sqlite3

#to make DB equivalent to the sqling file
DB = 'quiz.db'

#functions

#function for fetching all the necessary data
def initialize_data():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT id, questions, answers FROM questions")
    rows = cursor.fetchall()
    #give Them each a number value and save it as a list!!
    ids = [row[0] for row in rows]
    question = [row[1] for row in rows]
    answer = [row[2] for row in rows]
    return ids, question, answer

#function for adding question
def add_question():
    #fetch/get the data from initialize function into a new named variable
    ids, added_question, added_answer = initialize_data()
    #variable/maging letter for easy access for connecting to the database
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    #print Warning!
    print("BEWARE This is CASE SENSITIVE!!")

    #while true loop
    while True:
        #another while loop so that if this specific condition wanted to be repeated again⬇️
        
        while True:
            #ask what question they want
            question_input = input("Enter question: ").strip()
            #if they just press space or enter then print that it's invalid
            if len(question_input) <= 0:
                print("That's invalid, please enter a proper question ")
            #else append that to the list
            else:
                added_question.append(question_input)
                break

        #another while loop so that if this specific condition wanted to be repeated again⬇️
        while True:
            #answer for the question
            answer_input = input(f"Enter Answer for {added_question[-1]}:==>: ").strip()
            #if they enter none then print a warning and not append else append it
            if len(answer_input) <= 0: 
                print("Please Enter the Answer!")
            else:
                added_answer.append(answer_input)

                cursor.execute("INSERT INTO questions (questions, answers) VALUES (?, ?)", 
                               (question_input, answer_input))
                conn.commit()
                #create a new Id for the question !important for deleting them
                new_id = cursor.lastrowid
                ids.append(new_id)
                #print confirmation
                print(f"Successfully saved to database with ID: {new_id}!")
                break
            #ask if they want another question
        while True:
            confirmation = input("Do you want to continue? y/n: ").strip().lower()
            if confirmation == 'n':
                conn.close()
                main_menu()
                break
            elif confirmation == "y":
                add_question()
            else:
                print("Invalid Input!")

    conn.close()
    
    return ids, added_question, added_answer


    
#function for deleting question
def delete_question():
    #fetch the data
    ids, questions, answers = initialize_data()
    #if no id then go to add question function
    if len(ids) == 0:
        print("There are no questions in the database to delete.")
        add_question()
    #for loop to print the id and question so they can choose which one to delete
    for i in range(len(ids)):
        print(f"ID: {ids[i]} / Question: {questions[i]}")
    #easy accesv to connecting to DB
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    
    while True:
        #use try for invalid id
        try:
            #an input to remove the question using the id
            delete_id = int(input("Enter the id of the question you want to delete: "))
            #if it's in ids's list then continue
            if delete_id in ids:
                #delete the selected id that the user chose
                cursor.execute("DELETE FROM questions WHERE id = ?", (delete_id,))
                conn.commit() #commit and print a successful message
                print(f"Question with id {delete_id} successfully deleted.")
                break
            #if Id is invalid⬇️
            else:
                print("That id does not exist. Please pick an id from the list.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the id.")
            conn.close()

        #if they want to leave this domain or not
    while True:
        user = input("Continue? y/n").lower().strip()
        if user == "y":
            delete_question()
        elif user == "n":
            main_menu()
        else:
            print("Invalid! Enter the Appropriate Letter!")
        


#function viewing everithing
def view_all_question():
    question = initialize_data()
    print(question)

    #ask if they want to leave or not
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
            
            
#function for starting the quiz
def quiz():
    #fetch the data from database
    question = initialize_data()[1]
    answer = initialize_data()[2]
    question_t = len(question)
    #a variable to keep count of how many the user got correct
    correct = 0
    #if there's no question then print go to add Question
    if len(question) == 0:
        print("Add a question first!!!")
        add_question()
        return
    #a for loop to go to every question with the answer besides it
    for ques, ans in zip(question, answer):
        user_answer = input(f"{ques}: ")

        #If it's the same as the answer then print correct
        if (user_answer) == ans:
            print("Correct")
            #add 1 if they got one correct
            correct = correct + 1
        #if they get it wrong then print the right answer
        else:
            print(f"Wrong it's {ans}")
    print(f"You've got {correct} correct out of {question_t}")
    correct = 0

    #confirmation if they want to continue
    while True:
        user = input("\nRestart Quiz or Main Menu? y/n").lower().strip()
        if user == "y":
            quiz()
        elif user == "n":
            main_menu()
        else:
            print("\nInvalid! Please Enter Correct Letter")
            

# the main menu
def main_menu():
    print("""Main Menu
          1. Take Quiz
          2. Add Question
          3. Delete Question
          4. Exit
          5. View All Question""")
    #if they press a certain number then go to that doamin
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

#=====start the whole thing======#        
main_menu()

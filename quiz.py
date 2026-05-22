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

def check_answer():
    ids, question, answer = initialize_data()
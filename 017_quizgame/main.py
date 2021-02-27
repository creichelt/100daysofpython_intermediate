from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import os

# creating question bank from data
question_bank = []
for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))

# creating quiz object
quiz = QuizBrain(question_bank)

# looping through questions
while quiz.still_has_questions():
    quiz.next_question()

os.system('clear')
print("\nQuiz complete!")
print(f"Final score: {quiz.score} out of {quiz.q_number}\n")


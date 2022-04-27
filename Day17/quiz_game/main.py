from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

print('Welcome to the quiz game!\nPress "q" at anytime to quit.\n')

question_bank = []
for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))
    # question_text = question['text']
    # question_answer = question['answer']
    # question_bank.append(Question(text=question_text, answer=question_answer))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f'Your final score is: {quiz.score}/{quiz.question_num}.\n')
print('Thanks for playing!!!'.upper())

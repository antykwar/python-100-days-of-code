from pyinputplus import inputYesNo

from day17_modules.question import Question
from day17_modules.question_bank import QuestionBank
from day17_modules.data import question_data_set
from day17_modules.quiz_brain import QuizBrain

question_bank = QuestionBank()
for question_data in question_data_set:
    question_bank.add_question(Question(
        question_data['text'],
        question_data['answer']
    ))

quiz_brain = QuizBrain()
quiz_brain.set_question_bank(question_bank)

while True:
    question = quiz_brain.ask_question()

    if not question:
        print(f'You`ve answered all questions! Your score is {quiz_brain.get_total_score()}!')
        break

    answer = True if inputYesNo(question.text + ' (true/false) ', yesVal='true', noVal='false') == 'true' else False
    status = 'right' if answer else 'wrong'

    if question.is_correct(answer):
        quiz_brain.add_score()

    print(f'That`s {status}, your score is {quiz_brain.get_total_score()}.')

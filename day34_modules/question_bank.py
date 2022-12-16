import html
import requests

from .question import Question


class QuestionBank:
    def __init__(self):
        self.questions = []
        self.current_question_number = 0

    def add_question(self, question: Question):
        self.questions.append(question)

    def load_questions(self):
        questions = self._get_questions_block()
        for question in questions:
            self.add_question(Question(
                html.unescape(question['question']),
                (question['correct_answer'].lower() == 'true')
            ))

    def next(self):
        if self.current_question_number >= len(self.questions):
            return None
        question = self.questions[self.current_question_number]
        self.current_question_number += 1
        return question

    @staticmethod
    def _get_questions_block():
        params = {'amount': 10, 'type': 'boolean'}
        response = requests.get(url='https://opentdb.com/api.php', params=params)
        response.raise_for_status()
        questions = response.json()
        if questions['response_code'] != 0:
            return []
        return questions['results']

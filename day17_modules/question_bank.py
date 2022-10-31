from .question import Question


class QuestionBank:
    def __init__(self):
        self.questions = []
        self.current_question_number = 0

    def add_question(self, question: Question):
        self.questions.append(question)

    def length(self):
        return len(self.questions)

    def next(self):
        if self.current_question_number >= len(self.questions):
            return None
        question = self.questions[self.current_question_number]
        self.current_question_number += 1
        return question

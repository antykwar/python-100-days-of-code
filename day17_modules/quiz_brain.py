from .question_bank import QuestionBank


class QuizBrain:
    def __init__(self):
        self.question_bank = None
        self.score = 0

    def add_score(self):
        self.score += 1

    def set_question_bank(self, question_bank: QuestionBank):
        self.question_bank = question_bank

    def ask_question(self):
        return self.question_bank.next()

    def get_total_score(self):
        return f'{self.score}/{self.question_bank.length()}'

from .question_bank import QuestionBank


class QuizBrain:
    def __init__(self):
        self.question_bank = QuestionBank()
        self.question_bank.load_questions()
        self.score = 0
        self.total_questions_asked = 0

    def add_score(self):
        self.score += 1

    def ask_question(self):
        return self.question_bank.next()

    def get_total_score(self):
        return self.score

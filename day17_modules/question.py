class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def is_correct(self, answer):
        return self.answer == answer

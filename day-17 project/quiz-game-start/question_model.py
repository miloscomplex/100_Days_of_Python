class Question(object):
    """docstring for question."""

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


new_q = Question("asdef", "False")
print(new_q.text)

import base64 

class Puzzle:
    GAME_TYPE = 'Game type not defined.'

    def __init__(self):
        self._answer = 'N/A'
        self._question = 'No question defined.'

    def question(self):
        return self._question

    def answer(self):
        encoded = base64.b64encode(self._answer.encode('utf-8')).decode('utf-8')
        return f'Answer: https://josh-kaplan.github.io/puzzlebot/?{encoded}'
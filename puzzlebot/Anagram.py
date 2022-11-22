import random
from .Puzzle import Puzzle
from . import utils 


class Anagram(Puzzle):

    GAME_TYPE = 'Anagram'
    GAME_HELP = '''
    Solve the anagram by rearranging the letters to determine the original word. Read more about anagrams
    '''
    DIFFICULTY = 'EASY'

    def __init__(self):
        words = utils.get_data('words_curated.txt')
        word = random.choice(words)
        self._answer = word

        chars = [*word]
        random.shuffle(chars)
        anagram = ''.join(chars)
        self._question = f'Solve the anagram: {anagram}'


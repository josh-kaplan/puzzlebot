import random
from .Puzzle import Puzzle
from . import utils 


class Anagram(Puzzle):

    GAME_TYPE = 'Anagram'
    GAME_HELP = '''
    Solve the anagram by rearranging the letters to determine the original word. 
    There may be more than one solution. Read more about anagrams at https://en.wikipedia.org/wiki/Anagram.
    '''
    DIFFICULTY = 'EASY'

    def __init__(self):
        # Make the puzzle
        words = utils.get_data('words_curated.txt')
        index = utils.get_json('words_alpha_indexed.json')
        word = random.choice(words)

        key = utils.anagram_hash(word)
        ans = f'Our answer was "{word}". All possibilities are: ' + ', '.join(index[key])
        self._answer = ans

        chars = [*word]
        random.shuffle(chars)
        anagram = ''.join(chars)
        self._question = f'Solve the anagram: {anagram}'


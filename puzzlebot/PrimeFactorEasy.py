import random 
from .Puzzle import Puzzle
from . import utils 


class PrimeFactorEasy(Puzzle):

    GAME_TYPE = 'Prime Factors (Easy version)'
    GAME_HELP = '''
    Determine the prime factors of the given number. This is the easy version of
    this puzzle it only uses the first 100 primes.
    '''
    DIFFICULTY = 'EASY'

    def __init__(self):
        primes = utils.get_data('primes_10k.txt')[:100]
        N = int(random.choice(primes))
        M = int(random.choice(primes))
        self._answer = f'{N},{M}'

        P = N*M
        self._question = f'Find the prime factors: {P}'
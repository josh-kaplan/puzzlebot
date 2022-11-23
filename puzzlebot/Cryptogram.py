import random 
from .Puzzle import Puzzle
from . import utils 
from .ciphers import Ciphers


class Cryptogram(Puzzle):

    def __init__(self):
        self.GAME_TYPE = 'Cryptogram'
        self. GAME_HELP = '''
        This is a Cryptogram. The puzzle contains a phrase encrypted with a simple
        cipher. Determine the original phrase. Punctuation is not altered. 
        Read more about cryptograms at https://en.wikipedia.org/wiki/Cryptogram.
        '''
        self.DIFFICULTY = 'EASY / MEDIUM'

        ciphers = Ciphers.__all__()
        print(ciphers)
        Cipher = getattr(Ciphers, random.choice(ciphers))
        cipher = Cipher()
        print(cipher.name)
        print(cipher.key)

        # Get possible solutions as flat list
        phrases = []
        data = utils.get_json('corpora_words_us-president-quotes.json')
        for d in data['data']:
            for q in d['quotes']:
                phrases.append(q)
        
        self._answer = random.choice(phrases)

        enc = cipher.encrypt(self._answer)
        self._question = f'{enc}'
        #primes = utils.get_data('primes_10k.txt')[:100]
        #N = int(random.choice(primes))
        #M = int(random.choice(primes))
        #self._answer = f'{N},{M}'
#
        #P = N*M
        #self._question = f'Find the prime factors: {P}'
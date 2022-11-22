import argparse
import random
import datetime as dt
from mastodon import Mastodon
from .Anagram import Anagram
from .PrimeFactorEasy import PrimeFactorEasy


GAMES = [Anagram, PrimeFactorEasy]
WEIGHTS = [4, 1]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--access-token', required=True)
    args = parser.parse_args()

    body = ''
    now = dt.datetime.utcnow()
    datefmt = now.strftime('%A, %B %d, %Y')
    N = 1

    game = random.choices(GAMES, WEIGHTS, k=1)[0]()
    game_help = game.GAME_HELP.replace('    ', '').replace('\n', '')
    body += f'PuzzleBot {datefmt}\n\n'
    body += f'Puzzle Type: {game.GAME_TYPE}\n'
    body += f'Difficulty: {game.DIFFICULTY.lower()}\n'
    body += f'Instructions: {game_help}'
    body += '\n\n'
    body += game.question()
    body += '\n\n'
    body += game.answer()
    print(body)

    #mastodon = Mastodon(
    #    api_base_url = 'https://universeodon.com/',
    #    access_token = os.environ.get('MASTODON_ACCESS_TOKEN', '')
    #)

    # Post status
    
    #mastodon.toot('Tooting from Python using #mastodonpy !')


if __name__ == '__main__':
    main()
import argparse
import random
import datetime as dt
from mastodon import Mastodon
from .Anagram import Anagram
from .Anagram7 import Anagram7
from .PrimeFactorEasy import PrimeFactorEasy

# Configure the puzzles
GAMES = [Anagram, Anagram7, PrimeFactorEasy]
WEIGHTS = [50, 40, 10]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--access-token', required=True)
    parser.add_argument('--puzzle-type', required=False)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    body = ''
    now = dt.datetime.utcnow()
    label = 'Morning Puzzle' if now.hour < 12 else 'Afternoon Puzzle'
    datefmt = now.strftime(f'%A, %B %d, %Y - {label}')

    if args.puzzle_type == 'Anagram':
        game = Anagram()
    else:
        game = random.choices(GAMES, WEIGHTS, k=1)[0]()


    game_help = game.GAME_HELP.replace('    ', '').replace('\n', '')
    body += f'PuzzleBot {datefmt}\n\n'
    body += game.question()
    body += '\n\n' + '-'*40 + '\n\n'
    body += 'More about PuzzleBot at https://josh-kaplan.github.io/puzzlebot\n\n'
    body += f'Instructions: {game_help}\n\n'
    body += f'Difficulty: {game.DIFFICULTY}'
    body += '\n\n'
    
    body += game.answer()
    body += '\n\n'
    body += '#PuzzleBot #Puzzle'

    if args.dry_run:
        print(body)
    else:
        mastodon = Mastodon(
            api_base_url = 'https://universeodon.com/',
            access_token = args.access_token
        )

        # Post status
        mastodon.toot(body)
        print('Posted status.')


if __name__ == '__main__':
    main()
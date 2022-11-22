"""

Takes in a text files with words on each line and outputs a JSON file
where the keys are an ordered representation of letters and values
are a list of matching words.

"""
import sys
import json

def main():
    infile = sys.argv[1]
    outfile = sys.argv[2]

    print('Reading input file ...')
    words = open(infile).read().splitlines()

    print('Indexing ...')
    dictionary = {}
    for word in words:
        chars = sorted([*word])
        key = ''.join(chars)
        if key not in dictionary.keys():
            dictionary[key] = []
        dictionary[key].append(word)

    print('Writing file ...')
    with open(outfile, 'w') as f:
        f.write(json.dumps(dictionary, indent=4, sort_keys=True))

if __name__ == '__main__':
    main()
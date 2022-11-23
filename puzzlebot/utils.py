import os
import json


def get_data_dir():
    dirname = os.path.dirname(__file__)
    return os.path.abspath(os.path.join(dirname, '..', 'data'))


def get_data(fname):
    data_dir = get_data_dir()
    fpath = os.path.join(data_dir, fname)
    return open(fpath).read().splitlines()


def get_json(fname):
    data_dir = get_data_dir()
    fpath = os.path.join(data_dir, fname)
    return json.loads(open(fpath).read())


def anagram_hash(word):
    chars = sorted([*word])
    key = ''.join(chars)
    return key


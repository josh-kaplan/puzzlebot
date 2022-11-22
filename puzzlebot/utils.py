import os

def get_data_dir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

def get_data(fname):
    data_dir = get_data_dir()
    fpath = os.path.join(data_dir, fname)
    return open(fpath).read().splitlines()
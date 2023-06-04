import pickle

my_dict = {'a': 1, 'b': 2, 'c': 3}

class pickle_writer:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'wb')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# Usage:
with pickle_writer('my_dict.pkl') as f:
    pickle.dump(my_dict, f)
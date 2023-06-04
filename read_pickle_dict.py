import pickle

class pickle_reader:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'rb')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# Usage:
with pickle_reader('my_dict.pkl') as f:
    my_dict = pickle.load(f)

print(my_dict)
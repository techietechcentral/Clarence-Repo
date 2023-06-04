class file_writer:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# Usage:
with file_writer('test.txt') as f:
    f.write("Hello, I am a context manager!")
    
    
class file_reader:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# Usage:
with file_reader('test.txt') as f:
    contents = f.read()
    print(contents)
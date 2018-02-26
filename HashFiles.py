from hashlib import sha256
from os.path import isfile, join
from os import listdir


class HashFiles():
    def __init__(self):
        self.dirs = []

    def main(self):
        only_files = []

        only_files.extend(self.get_files('.\\'))
        # Cicle through and traverse dirs
        while len(self.dirs):
            current_dir = self.dirs.pop()
            only_files.extend(self.get_files(current_dir))

        if len(only_files) > 1:
            for f in only_files:
                if (f == '.\\HashFiles.py'):
                    continue
                hsh = self.hash_file(f)
                print(hsh)
        else:
            print('No files in directory!')

    # Gets the files of a directory, if no directory is passed gets root dir
    def get_files(self, path='', extension=''):
        only_files = []
        if(path):
            files = listdir(path)
        else:
            files = listdir()

        for f in files:
            if(path):
                f = join(path, f)
            # Checks if it's a file, if not appends to directories
            if isfile(f):
                only_files.append(f)
            else:
                self.dirs.append(f)

        return only_files

    # Hashes a file passed to it.
    def hash_file(self, file):
        sha = sha256()

        with open(file, 'rb') as f:
            while True:
                data = f.read(2 ** 20)
                if not data:
                    break
                sha.update(data)
        file_and_hash = file + ' : ' + sha.hexdigest()
        return file_and_hash


if __name__ == '__main__':
    hf = HashFiles()
    hf.main()

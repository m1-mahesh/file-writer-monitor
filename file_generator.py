import os
import random
import string
from utility import FileMonitor


class FileGenerator(FileMonitor):
    def __init__(self, path='./file-store', log_path="./logs"):
        super().__init__(path, log_path)

    @staticmethod
    def generate_words(number_of_words=100, word_len=5):
        for number in range(1, number_of_words):
            if number % 2 == 0:
                rand_num = random.randrange(-100, 25, 1)
                if rand_num < 0:
                    random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=word_len))
                    if 35 > number > 20:
                        random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=word_len - 3))
                        random_str = random_str + 'CDS'
                    elif 95 > number > 80:
                        random_str = 'CDS'.join(random.choices(string.ascii_uppercase + string.digits, k=word_len - 3))
                    yield random_str
                else:
                    yield 'CDS'
            else:
                yield 'CDS'

    def generate_files(self, file_count=2):
        for i in range(file_count):
            file_name = '{}/{}-{}.txt'.format(self._FILE_STORE_PATH, 'sample-file', i)
            with open(file_name, 'w') as f:
                for word in self.generate_words():
                    f.write('{} '.format(word))
                f.close()


if __name__ == '__main__':
    file_gen = FileGenerator()
    file_gen.generate_files()
    print('File generated successfully')



import codecs
import os
import chardet
import re
import collections
import sys


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'rb') as file_text:
            char_type = chardet.detect(file_text.read())['encoding']
        with codecs.open(filepath, 'rb', encoding=char_type) as file_text:
            return file_text.read()


def get_most_frequent_words(text):
    return collections.Counter(re.sub(r'[^\w\s]', '', text).split()).most_common(10)



if __name__ == '__main__':
    if sys.argv[1]:
        text_file = load_data(sys.argv[1])
    else:
        print('input path to file')
    print(get_most_frequent_words(text_file))


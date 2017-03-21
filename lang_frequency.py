import codecs
import os
import chardet
import re
import collections
import sys
import argparse

def create_parser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('filepath')
    parser.add_argument ('-c', '--cost_result', nargs='?') 
    return parser

def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'rb') as file_text:
            char_type = chardet.detect(file_text.read())['encoding']
        with codecs.open(filepath, 'rb', encoding=char_type) as file_text:
            return file_text.read()

def get_most_frequent_words(text, cost_result=10):
    return collections.Counter(re.sub(r'[^\w\s]', '', text).split()).most_common(cost_result)



if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    text_file = load_data(namespace.filepath)
    print(namespace)
    if namespace.cost_result:
        print(get_most_frequent_words(text_file, int(namespace.cost_result)))
    else:
        print(get_most_frequent_words(text_file))
    
   
 

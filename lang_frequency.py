import codecs
import os
import chardet
import re
import collections


def load_data(filepath):
    if os.path.exists(filepath):
        char_type = chardet.detect(open(filepath, "rb").read())['encoding']
        with codecs.open(filepath, 'rb', encoding=char_type) as file_text:
            return file_text.read()


def get_most_frequent_words(text):
    text_file = re.sub(r'[\.,\,,\?,\!,\-,\),\(,\–,\«,\»,\…,\[,\],\:,\;,\d]', '', text)
    list_words = text_file.split()
    word_count = collections.Counter()
    for word in list_words:
        word_count[word] += 1
    print(word_count.most_common()[:10])



if __name__ == '__main__':
    text_file = load_data('book1.txt')
    print(text_file)
    get_most_frequent_words(text_file)


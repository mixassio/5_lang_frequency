import codecs
import os
import chardet
import re


def load_data(filepath):
    if os.path.exists(filepath):
        char_type = chardet.detect(open(filepath, "rb").read())['encoding']
        with codecs.open(filepath, 'rb', encoding=char_type) as f, codecs.open("new.txt", 'wb', encoding='utf-8') as g:
            for i in f:
                print(i, file=g)
        with open('new.txt', 'r', encoding='utf-8') as fh:
            return fh.read()


def get_most_frequent_words(text):
    text_file = re.sub(r'[\.,\,,\?,\!,\-,\),\(,\–,\«,\»,\…,\[,\],\:,\;]', '', text)
    list_words = text_file.split()
    set_words = set(list_words)
    dict_cost_words = {}
    for word in set_words:
        dict_cost_words[word] = 1
    for word in list_words:
        dict_cost_words[word] += 1
    list_sort = sorted(dict_cost_words.items(), key=lambda x: x[1], reverse=True)
    for i in range (0, 10):
        print(list_sort[i])


if __name__ == '__main__':
    text_file = load_data('book1.txt')
    get_most_frequent_words(text_file)


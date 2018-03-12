import nltk
import re
import os
import pickle
import sys
from nltk.corpus import stopwords


def assert_dir(path):
    if not os.path.exists(path):
        print('ERROR: {} does not exists'.format(path))
        sys.exit(1)

    if not os.path.isdir(path):
        print('ERROR: {} is not a directory'.format(path))
        sys.exit(1)


def preprocess_text(text):
    processed_text = text.lower()
    processed_text = processed_text.replace("’", "'")
    processed_text = processed_text.replace("“", '"')
    processed_text = processed_text.replace("”", '"')

    non_words = re.compile(r"[^A-Za-z']+")
    processed_text = re.sub(non_words, ' ', processed_text)

    return processed_text


def get_text_from_file(filename):
    with open(filename, encoding='cp1252', mode='r') as f:
        text = f.read()

    return text


def get_words_from_text(text):
    stop_words = set(stopwords.words('english'))

    processed_text = preprocess_text(text)
    words = {w for w in processed_text.split() if w not in stop_words}

    return words


def build_inverted_index(docs_path):
    inverted_index = {}

    for doc_file in os.listdir(docs_path):
        filename = os.path.join(docs_path, doc_file)
        text = get_text_from_file(filename)
        words = get_words_from_text(text)

        for word in words:
            if inverted_index.get(word, None) is None:
                inverted_index[word] = {filename}
            else:
                inverted_index[word].add(filename)

    return inverted_index


def index(docs_path, data_path):
    inverted_index = build_inverted_index(docs_path)
    dic_file = os.path.join(data_path, 'dictionary.txt')
    inverted_index_file = os.path.join(data_path, 'inverted_index.pickle')

    with open(dic_file, mode='w') as f:
        for word in inverted_index.keys():
            f.write(word + '\n')

    with open(inverted_index_file, mode='wb') as f:
        pickle.dump(inverted_index, f)

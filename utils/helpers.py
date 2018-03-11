import nltk
import re
import os
from nltk.corpus import stopwords


def get_text_from_file(filename):
    with open(filename, encoding='cp1252', mode='r') as f:
        text = f.read()

    return text.lower()


def get_words_from_text(text):
    non_words = re.compile(r'[^A-Za-z]+')
    stop_words = set(stopwords.words('english'))

    processed_text = re.sub(non_words, ' ', text)
    words = {w for w in processed_text.split() if w not in stop_words}

    return words


def get_words_from_docs(docs_path):
    words = set()

    for doc_file in os.listdir(docs_path):
        filename = os.path.join(docs_path, doc_file)
        text = get_text_from_file(filename)
        words.update(get_words_from_text(text))

    return words


def store_words_from_docs_to_file(dic_file, docs_path):
    words = get_words_from_docs(docs_path)
    with open(dic_file, 'w') as f:
        for w in words:
            f.write(w + '\n')

from utils import helpers
import os

docs_path = os.path.join(os.getcwd(), 'docs')
dic_file = os.path.join(os.getcwd(), 'data', 'dictionary.txt')

helpers.store_words_from_docs_to_file(dic_file, docs_path)

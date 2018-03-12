import os
import re
import argparse
import pickle
import sys
from nltk.corpus import stopwords

# Get inverted index from pickle file
inverted_index_file = os.path.join(
    os.getcwd(), 'data', 'inverted_index.pickle')

with open(inverted_index_file, mode='rb') as f:
    inverted_index = pickle.load(f)

dictionary = inverted_index.keys()

non_words = re.compile(r"[^A-Za-z'?]+")
stop_words = set(stopwords.words('english'))

# Create a command line parser
parser = argparse.ArgumentParser(description='Boolean query')
parser.add_argument('query', help='words seperated by space')
args = parser.parse_args()

# Preprocess query
query = args.query
query = query.lower()
query = re.sub(non_words, ' ', query)

# Remove all stopwords and words which is not in dictionary
words = {
    word for word in query.split()
    if word not in stop_words and word in dictionary}

result = None
for word in words:
    if result is None:
        result = inverted_index.get(word)
    else:
        result.intersection_update(inverted_index.get(word))

print(result)

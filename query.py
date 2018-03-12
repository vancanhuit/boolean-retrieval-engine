import os
import argparse
import pickle
import sys

# Get inverted index from pickle file
inverted_index_file = os.path.join(
    os.getcwd(), 'data', 'inverted_index.pickle')

with open(inverted_index_file, mode='rb') as f:
    inverted_index = pickle.load(f)

dictionary = inverted_index.keys()

# Create a command line parser
parser = argparse.ArgumentParser(description='Boolean query')
parser.add_argument('query', help='words seperated by space')
args = parser.parse_args()

query = args.query
words = set(query.split())

result = None
for word in words:
    if word not in dictionary:
        print('The "{}" is not in dictionary'.format(word))
        sys.exit(1)
    elif result is None:
        result = inverted_index.get(word)
    else:
        result.intersection_update(inverted_index.get(word))

print(result)

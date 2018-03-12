import argparse
import os
import sys
import helpers


# Create a command line parser which accepts two positional arguments
parser = argparse.ArgumentParser(
    description='Index data for boolean retrieval')
parser.add_argument('docs_path', help='Directory for documents to be indexed')
parser.add_argument('data_path', help='Directory for storing indexed data')
args = parser.parse_args()

# Get arguments
docs_path = os.path.abspath(args.docs_path)
data_path = os.path.abspath(args.data_path)


helpers.assert_dir(docs_path)
helpers.assert_dir(data_path)

helpers.index(docs_path, data_path)
print('Index done.')

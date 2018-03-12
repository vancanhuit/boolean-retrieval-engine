# Simple boolean retrieval implementation with Python 3

## Prepare

- Install [Python 3.5+](https://www.python.org/)
- Install [NLTK 3](http://www.nltk.org/install.html)
- Open terminal / command prompt and enter following command:
    ```sh
    $ python
    >>> import nltk
    >>> nltk.download('stopwords')
    ```

# Usage

To index data, run `index.py` script and pass document's directory and directory for storing indexed data:

```sh
$ python index.py --help
usage: index.py [-h] docs_path data_path

Index data for boolean retrieval

positional arguments:
  docs_path   Directory for documents to be indexed
  data_path   Directory for storing indexed data

optional arguments:
  -h, --help  show this help message and exit

$ python index.py ./docs ./data
```

After indexing data successfully, run `query.py` script to perform query:

```sh
$ python query.py --help
usage: query.py [-h] query

Boolean query

positional arguments:
  query       words seperated by space

optional arguments:
  -h, --help  show this help message and exit

$ python query.py "popular available"
{'D:\\workspace\\boolean-retrieval-engine\\docs\\A Festival of Books.txt'}
```

When provide input for the query script, words must be seperated by space. For example, with input `"popular available"`, it's mean that find all documents which contain `popular` AND `available`. The returned result will be a set of documents satisfy the query. All numeric, punctuation and word which is not in dictionary will be ignored.

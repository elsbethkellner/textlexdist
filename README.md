# textlexdist

# Description

Library and CLI tool to find the shortest distance between 2 words, measured in words.

# Installation and Testing

## Create a virtualenv

```
virtualenv .venv --python=python3
source .venv/bin/activate
```

## Install and test

```
pip install -r requirements.txt
pytest
```

## CLI Usage

The script find_distance.py is used as follows:

usage: python find_distance.py [-h] filename word1 word2

Searches text in <filename> for the occurance of <word1> and <word2>,and
returns the distance between them, measured in words.

positional arguments:
  filename    filename of file search
  word1       first word to search for
  word2       second word to search for
  
### Use case

The canonical example 

`python find_distance.py tests/fixtures/example motivation development`



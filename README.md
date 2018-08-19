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


# Components and comments

The directory `textdist` contains the libraries for computing the feature.  The problem is broken down into 2 parts, implemented by the 2 components: the lexer and the algorithm to compute the distance.

The lexer `lexer.py` is responisble for turning a block of text (or a stream of text) into words.  I assumed English language to determine what constitutes a word, especially considering punctuation rules.  For instance, hypenated words are single words in English (mother-in-law, fleur-de-lys), but maybe not necessarily in German.  Perhaps that use case requires that "Simon-Dach-Strasse" be considered as 3 words.  The same applies to contractions ("can't", "won't).  Thus the class is separate and could be swapped.

The algorithm `finder.py` is commented and I believe clear from its implementation.  I made a couple small assumptions about the problem.  It was implicit in the description that the order the words appear does not matter. I would confirm this with product.  I also assumed that capitalization should not matter -- that we are looking for words, not strings.

The file `find_distance.py` is a command-line interface.

In the last commit, I changed the implementation to work with streams so that the code doesn't read the entire file contents into memory, and the command line tool uses this.  The function `find_shortest_distance` still works on string in memory, though.

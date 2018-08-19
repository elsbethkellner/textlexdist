import typing
import re


class UsageException(Exception):
    pass


class Lexer(object):
    """Class performs simple lexical analysis of text,
    creating an iterator of string from the input.
    The iterator returns strings which appear to be English words"""

    def __init__(self, text: str):
        if text is None:
            raise UsageException("No text specified")
        self.text = text

        # The following symbols can be considered word boundaries
        self.split_pattern = re.compile(r'[ \n\t".!?,()]')

    def iterate_words(self) -> typing.Iterator[str]:
        """Turn the text into an iterable of the words contained therein"""
        for lexical_item in re.split(self.split_pattern, self.text):
            if lexical_item != "":
                word = lexical_item.lower()
                yield word

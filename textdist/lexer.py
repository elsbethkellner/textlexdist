import typing
import re


class UsageException(Exception):
    pass


class Lexer(object):
    """Class performs simple lexical analysis of text,
    creating an iterator of string from the input.
    The iterator returns strings which appear to be English words"""

    def __init__(self, iter: typing.Iterator[str]):
        if iter is None:
            raise UsageException("No text specified")
        self.iter = iter

        # The following symbols can be considered word boundaries
        self.split_pattern = re.compile(r'[ \n\t".!?,()]')

    def iterate_words(self) -> typing.Iterator[str]:
        """Turn the text into an iterable of the words contained therein"""
        for text in self.iter:
            for lexical_item in re.split(self.split_pattern, text):
                if lexical_item != "":
                    word = lexical_item.lower()
                    yield word

    @classmethod
    def from_string(self, text: str):
        "Alternative constructor creates a Lexer from a string instead of stream"
        return Lexer(iter([text]))

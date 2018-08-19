import typing


class UsageException(Exception):
    pass


class Lexer(object):

    def __init__(self, text: str):
        if text is None:
            raise UsageException("No text specified")
        self.text = text

    def iterate_words(self) -> typing.Iterator[str]:
        """Turn the text into an iterable of the words contained therein"""
        # todo this is the naive approach just to see how close we are
        for line in self.text.split("\n"):
            for word in line.split(" "):
                yield word

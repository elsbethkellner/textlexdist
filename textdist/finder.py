from .lexer import Lexer, UsageException


def find_shortest_distance(text: str, word1: str, word2: str):
    """Finds the distance, measured in words, between word1 and word2 in the text.
    Order is not important (word2 may appear before word1)"""

    if not word1 or not word2:
        raise UsageException("Both search words must non-empty strings")

    lex = Lexer(text)
    last_word_seen = None
    shortest_distance = None
    current_distance = 0
    word1 = word1.lower()
    word2 = word2.lower()

    for word in lex.iterate_words():

        if word == word1 or word == word2:

            if last_word_seen and last_word_seen != word:
                # this branch is when we found both words
                assert (last_word_seen == word1 and word == word2) or \
                    (last_word_seen == word2 and word == word1), \
                    "Hit branch but last_word_seen=%s, word1=%s, word2=%s" % (
                        last_word_seen, word1, word2)

                # test if new shortest distance, and if so record
                if shortest_distance is None or current_distance < shortest_distance:
                    shortest_distance = current_distance
                    if shortest_distance == 0:  # short-circuit possible
                        return shortest_distance

            # we found at least one of the two words, so in all cases the search resets;
            # the next word we find will match with this word, not last_word_seen
            last_word_seen = word
            current_distance = 0
        else:
            current_distance += 1

    return shortest_distance

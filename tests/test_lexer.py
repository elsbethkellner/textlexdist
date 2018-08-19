from textdist.lexer import Lexer


def test_whitespace():
    "tests that empty strings are not returned as words"
    lex = Lexer("foo  bar")
    lst = [w for w in lex.iterate_words()]
    assert lst == ["foo", "bar"]


def test_newlines():
    "tests that newlines are treated as whitesapce"
    lex = Lexer("foo\nbar")
    lst = [w for w in lex.iterate_words()]
    assert lst == ["foo", "bar"]


def test_empty():
    "tests null input"
    lex = Lexer("")
    assert [] == list(lex.iterate_words())


def test_capitalization():
    "tests that capitalization doesn't matter"
    lex = Lexer("All")
    assert "all" == next(lex.iterate_words())


def test_compound_word():
    lex = Lexer("mother-in-law")
    assert "mother-in-law" == next(lex.iterate_words())


def test_punctuation_removal():
    "tests removal of punctuation which is not part of the word"
    lex = Lexer("no!")
    assert "no" == next(lex.iterate_words())
    lex = Lexer("yes.")
    assert "yes" == next(lex.iterate_words())
    lex = Lexer("yes, please")
    assert ["yes", "please"] == list(lex.iterate_words())


def test_quotation_mark_removal():
    "tests that quoted words should be unquoted"
    lex = Lexer('"title"')
    assert "title" == next(lex.iterate_words())


def test_trailing_apostrophe():
    """tests if possessives and slang are their own words
    Note this is not specified by the problem spec,
    but it matches singular possessive behavior (both "parent's" and "parents'") are words
    and the rules of English ("nothin'") is slang and will appear"""
    lex = Lexer("parents'")
    assert "parents'" == next(lex.iterate_words())
    lex = Lexer("nothin'")
    assert "nothin'" == next(lex.iterate_words())


def test_sentences():
    "tests two sentences, the use case from problem description"
    sentence = ("We do value and reward motivation in our development team.  "
                "Development is a key skill for a DevOp")
    lex = Lexer(sentence)
    actual = [w for w in lex.iterate_words()]
    expected = ["we", "do", "value", "and", "reward", "motivation",
                "in", "our", "development", "team",
                "development", "is", "a", "key", "skill", "for", "a", "devop"]
    assert actual == expected

import pytest

from textdist.finder import find_shortest_distance, find_shortest_distance_iterator
from textdist.lexer import UsageException


@pytest.fixture
def example_sentence():
    """A pytest fixture for the example test data.  Some might consider this
    simple to actually need a fixture, and indeed a module level variable would work,
    but it demonstrates fixture usage."""
    sentence = ("We do value and reward motivation in our development team.  "
                "Development is a key skill for a DevOp")
    return sentence


def test_adjacent():
    "tests simplest positive case of adjacent words"
    assert find_shortest_distance("foo bar", "foo", "bar") == 0


def test_substring_non_match():
    "tests substring does not result in a match"
    assert find_shortest_distance("foo foobar bar", "foo", "bar") == 1


def test_not_found(example_sentence):
    "tests output when input is absent from body"
    # no word found
    assert find_shortest_distance(example_sentence, "foo", "bar") is None
    # one of two words found
    assert find_shortest_distance(example_sentence, "motivation", "duckies") is None


def test_happy_path(example_sentence):
    "tests the use case from the problem description"
    assert find_shortest_distance(example_sentence, "motivation", "development") == 2


def test_reverse_order(example_sentence):
    """tests if the target words are given in the reverse order
    (compared to how they appear in the test)"""
    assert find_shortest_distance(example_sentence, "development", "motivation") == 2


def test_raises_on_null_input():
    "tests bad search body will raise"
    with pytest.raises(UsageException):
        find_shortest_distance_iterator(None, "foo", "bar")


def test_raises_on_empty_search():
    "tests empty search term will raise"
    with pytest.raises(UsageException):
        find_shortest_distance_iterator(
            ["text body to search"],
            "foo", "")


def test_search_for_same_word(example_iter):
    """tests when we search for the same word twice,
    we should find distance between 2 different instances of the word"""
    assert find_shortest_distance_iterator(
        example_iter, "development", "development") == 1


def test_search_for_same_word_no_match(example_iter):
    """tests when we search for the same word twice,
    if the word appears once, this is no match"""
    assert find_shortest_distance_iterator(
        example_iter, "motivation", "motivation") is None

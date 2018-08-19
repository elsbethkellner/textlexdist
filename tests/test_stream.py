from textdist.finder import find_shortest_distance_iterator


def test_stream(example_iter):
    "test we can operate on the file stream without reading the entire file into memory"

    distance = find_shortest_distance_iterator(example_iter, "motivation", "development")
    assert distance == 2

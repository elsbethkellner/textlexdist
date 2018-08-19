import pytest
import os

from textdist.finder import iterator_from_file


@pytest.fixture
def example_iter():
    "pytest fixture for opening a test file on disk"

    fixture = os.path.join(os.path.dirname(__file__), "fixtures", "example")
    assert os.path.exists(fixture)
    with open(fixture) as fd:
        yield iterator_from_file(fd)

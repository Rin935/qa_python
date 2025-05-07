import pytest

from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        return BooksCollector()
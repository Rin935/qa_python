import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.fixture
    def collector(self):
        return BooksCollector()

    def test_add_new_book_valid_name(self, collector):
        collector.add_new_book("Цветы для Элджернона")
        assert "Цветы для Элджернона" in collector.books_genre


    def test_add_new_book_duplicate(self, collector):
        collector.add_new_book("Унесённые ветром")
        collector.add_new_book("Унесённые ветром")
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize(
        "name",
        [
            "",
            "Две мелодии сердца. Путеводитель оптимистки с разбитым сердцем"
        ]
    )
    def test_add_new_book_invalid_name(self, collector, name):
        collector.add_new_book(name)
        assert name not in collector.books_genre

    def test_set_book_genre_valid(self, collector):
        collector.add_new_book("Зов Ктулху")
        collector.set_book_genre("Зов Ктулху", "Ужасы")
        assert collector.get_book_genre("Зов Ктулху") == "Ужасы"

    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book("Население: одна")
        collector.set_book_genre("Население: одна", "Хоррор")
        assert collector.get_book_genre("Население: одна") == ""

    def test_get_books_for_children(self, collector):
        collector.add_new_book("Дядя Фёдор, пёс и кот")
        collector.set_book_genre("Дядя Фёдор, пёс и кот", "Мультфильмы")
        collector.add_new_book("Зов Ктулху")
        collector.set_book_genre("Зов Ктулху", "Ужасы")
        children_books = collector.get_books_for_children()
        assert "Дядя Фёдор, пёс и кот" in children_books
        assert "Зов Ктулху" not in children_books

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        assert "Война и мир" in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_in_books_genre(self, collector):
        collector.add_book_in_favorites("Такой книги нет")
        assert "Такой книги нет" not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Униженные и оскоблённые")
        collector.add_book_in_favorites("Униженные и оскоблённые")
        collector.delete_book_from_favorites("Униженные и оскоблённые")
        assert "Униженные и оскоблённые" not in collector.get_list_of_favorites_books()
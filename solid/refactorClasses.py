from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class BookFormatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass


class TextFormatter(BookFormatter):
    def format(self, book: Book) -> str:
        return book.content


class Printer:
    def __init__(self, formatter: BookFormatter):
        self.formatter = formatter

    def get_book(self, book: Book) -> str:
        formatted_book = self.formatter.format(book)
        return formatted_book


book = Book('I am coding')
formatter = TextFormatter()
printer = Printer(formatter)
print(printer.get_book(book))
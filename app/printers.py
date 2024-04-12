from abc import ABC, abstractmethod


class Printer(ABC):

    @staticmethod
    @abstractmethod
    def print_book(book_title: str, book_content: str) -> None:
        pass


class ConsolePrint(Printer):

    @staticmethod
    def print_book(book_title: str, book_content: str) -> None:
        print(f"Printing the book: {book_title}...")
        print(book_content)


class ReversePrint(Printer):

    @staticmethod
    def print_book(book_title: str, book_content: str) -> None:
        print(f"Printing the book in reverse: {book_title}...")
        print(book_content[::-1])

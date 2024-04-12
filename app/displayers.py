from abc import ABC, abstractmethod


class Displayer(ABC):

    @staticmethod
    @abstractmethod
    def display(book_content: str) -> None:
        pass


class ConsoleDisplayer(Displayer):

    @staticmethod
    def display(book_content: str) -> None:
        print(book_content)


class ReverseDisplayer(Displayer):

    @staticmethod
    def display(book_content: str) -> None:
        print(book_content[::-1])

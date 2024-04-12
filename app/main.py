from app.displayers import ConsoleDisplayer, ReverseDisplayer
from app.printers import ConsolePrint, ReversePrint
from app.serializers import JsonSerializer, XmlSerializer


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                displayer = ConsoleDisplayer()

            elif method_type == "reverse":
                displayer = ReverseDisplayer()

            else:
                raise ValueError(f"Unknown display type: {method_type}")

            displayer.display(book.content)

        elif cmd == "print":
            if method_type == "console":
                printer = ConsolePrint()

            elif method_type == "reverse":
                printer = ReversePrint()

            else:
                raise ValueError(f"Unknown print type: {method_type}")

            printer.print_book(book.title, book.content)

        elif cmd == "serialize":
            if method_type == "json":
                serializer = JsonSerializer()

            elif method_type == "xml":
                serializer = XmlSerializer()

            else:
                raise ValueError(f"Unknown serialize type: {method_type}")

            return serializer.serialize_book(book.title, book.content)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))

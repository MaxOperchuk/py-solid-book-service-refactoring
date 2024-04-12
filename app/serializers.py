import json
import xml.etree.ElementTree as eT
from abc import ABC, abstractmethod


class Serializer(ABC):

    @staticmethod
    @abstractmethod
    def serialize_book(book_title: str, book_content: str) -> None:
        pass


class JsonSerializer(Serializer):

    @staticmethod
    def serialize_book(book_title: str, book_content: str) -> str:
        return json.dumps({"title": book_title, "content": book_content})


class XmlSerializer(Serializer):

    @staticmethod
    def serialize_book(book_title: str, book_content: str) -> str:
        root = eT.Element("book")
        title = eT.SubElement(root, "title")
        title.text = book_title
        content = eT.SubElement(root, "content")
        content.text = book_content
        return eT.tostring(root, encoding="unicode")

from __future__ import annotations
from .note import Note


class SourceNote(Note):
    _current_types: set[str] = {"book", "video", "magazine", "newspaper", "article", "lecture"}
    def __init__(self)-> None:
        super().__init__()
        self.author: str = ""
        self.source_type: str = ""  # "book", "podcast", etc

    def get_author(self) -> str:
        return self.author

    def set_author(self, author: str) -> None:
        if isinstance(author, str):
            self.author = author
        else:
            raise TypeError

    def get_source_type(self) -> str:
        return self.source_type

    def set_source_type(self, source_type: str) -> None:
        if isinstance(source_type, str):
            source_type = source_type.strip().lower()
            SourceNote._current_types.add(source_type)
            self.source_type = source_type
        else:
            raise TypeError

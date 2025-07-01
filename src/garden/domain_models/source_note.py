from __future__ import annotations
from typing import TYPE_CHECKING
from .note import Note

if TYPE_CHECKING:
    pass


class SourceNote(Note):
    def __init__(self)-> None:
        super().__init__()
        self.source_name: str = ""
        self.source_notes: str = ""
        self.author: str = ""
        self.source_type: str = ""  # "book", "podcast", etc

    def get_source_notes(self) -> str:
        return self.source_notes

    def set_source_notes(self, raw_notes: str) -> None:
        if isinstance(raw_notes, str):
            self.source_notes = raw_notes
        else:
            raise TypeError

    def get_author(self) -> str:
        return self.author

    def set_author(self, author: str) -> None:
        if isinstance(author, str):
            self.author = author
        else:
            raise TypeError

    def get_source_type(self) -> str:
        pass

    def set_source_type(self, source_type: str) -> None:
        pass

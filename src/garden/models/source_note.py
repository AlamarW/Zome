from __future__ import annotations
from typing import TYPE_CHECKING
from .note import Note

if TYPE_CHECKING:
    pass


class SourceNote(Note):
    def __init__(self)-> None:
        super().__init__()
        self.source_name: str = ""
        self.raw_notes: str = ""
        self.author: str = ""
        self.source_type: str = ""  # "book", "podcast", etc

    def get_raw_notes(self) -> str:
        pass

    def set_raw_notes(self, raw_notes: str) -> None:
        pass

    def get_author(self) -> str:
        pass

    def set_author(self, author: str) -> None:
        pass

    def get_source_type(self) -> str:
        pass

    def set_source_type(self, source_type: str) -> None:
        pass

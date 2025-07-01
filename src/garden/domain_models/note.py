from __future__ import annotations
from typing import TYPE_CHECKING
import re
from .base_class import BaseClass
from .nlp_processor import NLPProcessor

if TYPE_CHECKING:
    from .source_note import SourceNote
    from .attachment import Attachment
    from .draft import Draft


class Note(BaseClass):
    def __init__(self)->None:
        super().__init__()
        self.name: str = ""
        self.text: str = ""
        self.high_frequency_words: dict[str, int] = {}
        self.unique_words: list[str] = []  # words that are uncommon
        self.themes: list[str] = []
        self.source: list["SourceNote"] = []
        self.attachment: list["Attachment"] = []
        self.draft: list["Draft"] = []

    def set_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Note.name must be a string")
        elif re.match(r"^[a-zA-Z0-9 .\-?!']+$", name):
            self.name = name
        else:
            raise ValueError(
                "Note.name should only be alphanumeric, space dash period or question mark"
            )

    def get_name(self) -> str:
        return self.name

    def set_text(self, text: str = "") -> None:
        if not isinstance(text, str):
            raise TypeError("Note.text should be a string")

        else:
            self.text = text
            self.set_high_frequency_words()
            self.set_themes()

    def get_text(self) -> str:
        return self.text

    def get_high_frequency_words(self) -> dict[str, int]:
        return self.high_frequency_words

    def set_high_frequency_words(self) -> None:
        if not self.text or not isinstance(self.text, str):
            self.high_frequency_words = {}

        # Basic stop words
        clean_text = NLPProcessor.text_clean(self.text)
        hfw = NLPProcessor.calculate_high_frequency_words(clean_text)
        self.high_frequency_words = hfw

    def get_themes(self) -> list[str]:
        return self.themes

    def set_themes(self) -> None:
        if not self.text or not isinstance(self.text, str):
            self.themes = []
        themes = NLPProcessor.determine_themes(self.text)
        self.themes = themes

"""
    def get_source(self) -> list["SourceNote"]:
        pass

    def set_source(self, source: list["SourceNote"]) -> None:
        pass

    def get_attachment(self) -> list["Attachment"]:
        pass

    def set_attachment(self, attachment: list["Attachment"]) -> None:
        pass

    def get_draft(self) -> list["Draft"]:
        pass

    def set_draft(self, draft: list["Draft"]) -> None:
        pass

    def find_similar_notes(self, notes: list["Note"]) -> list["Note"]:
        pass

    def get_notes_by_themes(self, themes: str, notes: list["Note"]) -> list["Note"]:
        pass

    def find_connections_by_words(self, notes: list["Note"]) -> list["Note"]:
        pass

    def update_nlp_data(self) -> None:
        pass
"""

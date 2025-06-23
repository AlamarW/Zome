from typing import List, Dict, TYPE_CHECKING
import re
from .base_class import BaseClass
from .nlp_processor import NLPProcessor

if TYPE_CHECKING:
    from .tag import Tag
    from .source_note import SourceNote
    from .attachment import Attachment
    from .draft import Draft


class Note(BaseClass):
    def __init__(self):
        super().__init__()
        self.name: str = ""
        self.text: str = ""
        self.high_frequency_words: Dict[str, int] = {}
        self.unique_words: List[str] = []  # words that are uncommon
        self.theme: List[str] = []
        self.source: List["SourceNote"] = []
        self.attachment: List["Attachment"] = []
        self.draft: List["Draft"] = []

    def set_name(self, name: str) -> None:
        if not isinstance(name, str):
            self.name = (False, "Note.name must be a string")
        elif re.match(r"^[a-zA-Z0-9 .\-?!']+$", name):
            self.name = name
        else:
            self.name = (
                False,
                "Name can only include numbers letters, spaces, dashes (-), and regular punctuation",
            )

    def get_name(self) -> str:
        return self.name

    def set_text(self, text: str = "") -> None:
        if not isinstance(text, str):
            self.text = (False, "Note must be a string")
        else:
            self.text = text
            self.set_high_frequency_words()
            self.set_theme()

    def get_text(self) -> str:
        return self.text

    def get_high_frequency_words(self) -> Dict[str, int]:
        return self.high_frequency_words

    def set_high_frequency_words(self) -> Dict[str, int]:
        if not self.text or not isinstance(self.text, str):
            self.high_frequency_words = {}

        # Basic stop words
        clean_text = NLPProcessor.text_clean(self.text)
        hfw = NLPProcessor.calculate_high_frequency_words(clean_text)
        self.high_frequency_words = hfw

    def get_themes(self) -> str:
        pass

    def set_theme(self) -> None:
        if not self.text or not isinstance(self.text, str):
            self.theme = []
        theme = NLPProcessor.determine_themes(self.text)
        self.theme = theme

    def get_source(self) -> List["SourceNote"]:
        pass

    def set_source(self, source: List["SourceNote"]) -> None:
        pass

    def get_attachment(self) -> List["Attachment"]:
        pass

    def set_attachment(self, attachment: List["Attachment"]) -> None:
        pass

    def get_draft(self) -> List["Draft"]:
        pass

    def set_draft(self, draft: List["Draft"]) -> None:
        pass

    def find_similar_notes(self, notes: List["Note"]) -> List["Note"]:
        pass

    def get_notes_by_theme(self, theme: str, notes: List["Note"]) -> List["Note"]:
        pass

    def find_connections_by_words(self, notes: List["Note"]) -> List["Note"]:
        pass

    def update_nlp_data(self) -> None:
        pass

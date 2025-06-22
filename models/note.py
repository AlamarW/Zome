from typing import List, Dict, TYPE_CHECKING
import re
import string
from .base_class import BaseClass

if TYPE_CHECKING:
    from .tag import Tag
    from .source_note import SourceNote
    from .attachment import Attachment
    from .draft import Draft


class Note(BaseClass):
    _stop_words = None

    def __init__(self):
        super().__init__()
        self.name: str = ""
        self.text: str = ""
        self.high_frequency_words: Dict[str, int] = {}
        self.unique_words: List[str] = []  # words that are uncommon
        self.theme: str = ""
        self.source: List["SourceNote"] = []
        self.attachment: List["Attachment"] = []
        self.draft: List["Draft"] = []

    @staticmethod
    def _get_stop_words() -> None:
        if Note._stop_words is None:
            with open("stop_words_english.txt", "r") as f:
                Note._stop_words = set(word.strip().lower() for word in f)

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
            self._set_high_frequency_words()

    def get_text(self) -> str:
        return self.text

    def get_high_frequency_words(self) -> Dict[str, int]:
        return self.high_frequency_words

    def _set_high_frequency_words(self) -> Dict[str, int]:
        if not self.text or not isinstance(self.text, str):
            return self.high_frequency_words

        # Basic stop words
        stop_words = self._get_stop_words()
        text_clean = self.text.translate(str.maketrans("", "", string.punctuation))
        words = text_clean.lower().split()
        non_trivial_words = [w for w in words if w not in self._stop_words]

        word_count = {}

        # stemming words and counting
        for word in non_trivial_words:
            if len(word) > 1:
                root_word = word
                if word.endswith("ing") and len(word) > 4:
                    root_word = word[:-3]
                elif word.endswith("ed") and len(word) > 4:
                    root_word = word[:-2]

                word_count[root_word] = word_count.get(root_word, 0) + 1

        frequent_words = {}
        for word, count in word_count.items():
            if count > 1:
                frequent_words[word] = count

        # Sort by frequency (descending), then alphabetically
        sorted_words = dict(sorted(frequent_words.items(), key=lambda x: (-x[1], x[0])))

        self.high_frequency_words = sorted_words
        return self.high_frequency_words

    def get_themes(self) -> str:
        pass

    def set_theme(self, theme: str) -> None:
        pass

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

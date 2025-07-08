from typing import TYPE_CHECKING
from .base_class import BaseClass

if TYPE_CHECKING:
    pass


class Draft(BaseClass):
    APPROVED_TYPES = {"essay", "article", "story", "novel", "journal"}
    def __init__(self)-> None:
        super().__init__()
        self.name: str = ""
        self.type: str = ""  # "essay", "story", etc
        self.text: str = ""

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError

    def get_type(self) -> str:
        return self.type

    def set_type(self, draft_type: str) -> None:
        if isinstance(draft_type, str):
            if draft_type.lower() in self.APPROVED_TYPES:
                self.type = draft_type
            else:
                self.type = ""
        else:
            raise TypeError

    @classmethod
    def show_allowed_types(cls)-> set[str]:
       return cls.APPROVED_TYPES 

    def set_text(self, text: str) -> None:
        if isinstance(text, str):
            self.text = text
        else:
            raise TypeError

    def get_text(self) -> str:
        return self.text

from typing import TYPE_CHECKING
from .base_class import BaseClass

if TYPE_CHECKING:
    pass


class Draft(BaseClass):
    def __init__(self):
        super().__init__()
        self.name: str = ""
        self.type: str = ""  # "essay", "story", etc
        self.text: str = ""

    def get_name(self) -> str:
        pass

    def set_name(self, name: str) -> None:
        pass

    def get_type(self) -> str:
        pass

    def set_type(self, draft_type: str) -> None:
        pass

    def set_text(self, text: str) -> None:
        pass

    def get_text(self) -> str:
        pass
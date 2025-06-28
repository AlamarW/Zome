from typing import TYPE_CHECKING
from .base_class import BaseClass

if TYPE_CHECKING:
    pass


class Theme(BaseClass):
    def __init__(self)-> None:
        super().__init__()
        self.name: str = ""

    def get_name(self) -> str:
        pass

    def set_name(self, name: str) -> None:
        pass

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .note import Note
    from .source_note import SourceNote
    from .draft import Draft


class Attachment:
    def __init__(self):
        self.attachment: str = ""  # path to attachment
        self.note: List['Note'] = []
        self.source: List['SourceNote'] = []
        self.draft: List['Draft'] = []

    def set_attachment(self, path: str) -> None:
        pass

    def get_attachment(self) -> str:
        pass
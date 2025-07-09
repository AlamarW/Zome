from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .note import Note
    from .source_note import SourceNote
    from .draft import Draft


class Attachment:
    def __init__(self)-> None:
        self.attachment: str = ""  # path to attachment
        self.note: list['Note'] = []
        self.source: list['SourceNote'] = []
        self.draft: list['Draft'] = []

    def set_attachment(self, path: str) -> None:
        if isinstance(path, str):
            self.attachment = path

    def get_attachment(self) -> str:
        return self.attachment

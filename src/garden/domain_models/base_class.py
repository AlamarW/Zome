from typing import TYPE_CHECKING
import uuid
from datetime import datetime

if TYPE_CHECKING:
    from .tag import Tag


class BaseClass:
    def __init__(self) -> None:
        self.uuid: uuid.UUID = uuid.uuid4()
        self.date_created: datetime = datetime.now()
        self.date_edited: datetime = datetime.now()
        self.tags: list[str] = []

    def set_uuid(self, uuid: uuid.UUID) -> None:
        pass

    def get_uuid(self) -> uuid.UUID:
        return self.uuid

    def set_date_created(self, date: datetime) -> None:
        pass

    def get_date_created(self) -> datetime:
        pass

    def set_date_edited(self, date: datetime) -> None:
        pass

    def get_date_edited(self) -> datetime:
        pass

    def get_tags(self) -> list["Tag"]:
        pass

    def set_tags(self, tags: str) -> None:
        tags = tags.split()
        tags = [f"#{tag.title()}" if tag[0] != "#" else f"{tag.title()}" for tag in tags]
        self.tags = tags

    def add_tag(self, tag: "Tag") -> None:
        pass

    def remove_tag(self, tag: "Tag") -> None:
        pass

    def find_tag_connections(self, entities: list["BaseClass"]) -> list["Connection"]:
        pass

    def find_word_connections(self, entities: list["BaseClass"]) -> list["Connection"]:
        pass

    def find_theme_connections(self, entities: list["BaseClass"]) -> list["Connection"]:
        pass

    def get_all_connections(self) -> list["Connection"]:
        pass


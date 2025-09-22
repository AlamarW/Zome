from typing import TYPE_CHECKING
import uuid
from datetime import datetime


class BaseClass:
    def __init__(self) -> None:
        self.uuid: uuid.UUID = uuid.uuid4()
        self.date_created: datetime = datetime.now()
        self.date_edited: datetime = datetime.now()
        self.tags: set[str] = []

    def get_uuid(self) -> uuid.UUID:
        return self.uuid

    def set_date_created(self, date: datetime) -> datetime:
        self.date_created = date

    def get_date_created(self) -> datetime:
        return self.date_created

    def set_date_edited(self, date: datetime) -> datetime:
        self.date_edited = date

    def get_date_edited(self) -> datetime:
        return self.date_edited

    def get_tags(self) -> list[str]:
        return self.tags

    @staticmethod
    def _tag_formatter(tag: str) -> str:
        if tag[0] != "#":
            tag = f"#{tag}"

        return tag.title()

    def set_tags(self, tags: str) -> None:
        if isinstance(tags, str):
            tag_list = set(tags.split())
            tag_list = {self._tag_formatter(tag) for tag in tag_list}
            self.tags = tag_list
        else:
            raise TypeError

    def add_tag(self, tag: str) -> None:
        if isinstance(tag, str):
            tag = self._tag_formatter(tag)
            self.tags.add(tag)
        else:
            raise TypeError

    def remove_tag(self, tag: str) -> None:
        f_tag = self._tag_formatter(tag)
        self.tags.remove(f_tag)

    def compare_equal_tags(self, other) -> bool:
        return self.tags == other.tags

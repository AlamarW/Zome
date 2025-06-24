from typing import List, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from .connection import Connection
    from .tag import Tag


class BaseClass:
    def __init__(self):
        self.uuid: int = 0
        self.date_created: datetime = datetime.now()
        self.date_edited: datetime = datetime.now()
        self.tags: List['Tag'] = []

    def set_uuid(self, uuid: int) -> None:
        pass

    def get_uuid(self) -> int:
        pass

    def set_date_created(self, date: datetime) -> None:
        pass

    def get_date_created(self) -> datetime:
        pass

    def set_date_edited(self, date: datetime) -> None:
        pass

    def get_date_edited(self) -> datetime:
        pass

    def get_tags(self) -> List['Tag']:
        pass

    def set_tags(self, tags: List['Tag']) -> None:
        pass

    def add_tag(self, tag: 'Tag') -> None:
        pass

    def remove_tag(self, tag: 'Tag') -> None:
        pass

    def find_tag_connections(self, entities: List['BaseClass']) -> List['Connection']:
        pass

    def find_word_connections(self, entities: List['BaseClass']) -> List['Connection']:
        pass

    def find_theme_connections(self, entities: List['BaseClass']) -> List['Connection']:
        pass

    def get_all_connections(self) -> List['Connection']:
        pass
from typing import List, TYPE_CHECKING
from .base_class import BaseClass
from .connection import Connection

if TYPE_CHECKING:
    pass


class ConnectionManager:
    def __init__(self):
        self.all_entities: List[BaseClass] = []
        self.all_connections: List[Connection] = []

    def discover_connections(self) -> None:
        pass

    def create_tag_connection(self, entities: List[BaseClass]) -> Connection:
        pass

    def create_word_connection(self, entities: List[BaseClass]) -> Connection:
        pass

    def create_theme_connection(self, entities: List[BaseClass]) -> Connection:
        pass

    def update_all_connections(self) -> None:
        pass

    def get_connections_for_entity(self, entity: BaseClass) -> List[Connection]:
        pass

    def get_strongest_connections(self, limit: int = 10) -> List[Connection]:
        pass
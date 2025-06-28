from typing import TYPE_CHECKING
from .base_class import BaseClass
from .connection import Connection

if TYPE_CHECKING:
    pass


class ConnectionManager:
    def __init__(self):
        self.all_entities: list[BaseClass] = []
        self.all_connections: list[Connection] = []

    def discover_connections(self) -> None:
        pass

    def create_tag_connection(self, entities: list[BaseClass]) -> Connection:
        pass

    def create_word_connection(self, entities: list[BaseClass]) -> Connection:
        pass

    def create_theme_connection(self, entities: list[BaseClass]) -> Connection:
        pass

    def update_all_connections(self) -> None:
        pass

    def get_connections_for_entity(self, entity: BaseClass) -> list[Connection]:
        pass

    def get_strongest_connections(self, limit: int = 10) -> list[Connection]:
        pass

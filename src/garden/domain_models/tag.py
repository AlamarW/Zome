from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .connection import Connection


class Tag:
    def __init__(self)-> None:
        self.name: str = ""
        self.connections: list['Connection'] = []

    def get_connections(self) -> list['Connection']:
        pass

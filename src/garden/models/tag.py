from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .connection import Connection


class Tag:
    def __init__(self):
        self.name: str = ""
        self.connections: List['Connection'] = []

    def get_connections(self) -> List['Connection']:
        pass
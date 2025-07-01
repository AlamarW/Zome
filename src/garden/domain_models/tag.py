from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .connection import Connection


class Tag:
    def __init__(self)-> None:
        self.tag_name: str = ""
        self.connections: list['Connection'] = []

    def set_tag_name(self, tag_name:str):
        if tag_name[0] != "#":
            tag_name = f"#{tag_name}"
        self.tag_name = tag_name

    def get_tag_name(self):
        return self.tag_name

    def get_connections(self) -> list['Connection']:
        pass

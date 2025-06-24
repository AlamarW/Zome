from typing import List, Dict, Any, TYPE_CHECKING
from .base_class import BaseClass

if TYPE_CHECKING:
    pass


class Connection(BaseClass):
    def __init__(self):
        super().__init__()
        self.name: str = ""
        self.connection_type: str = ""  # "tag_similarity", "word_overlap", "theme_match", "citation"
        self.strength: float = 0.0  # 0.0 to 1.0
        self.entities: List[BaseClass] = []
        self.metadata: Dict[str, Any] = {}  # {"shared_tags": ["research", "AI"], "word_count": 15}

    def add_entity(self, entity: BaseClass) -> None:
        pass

    def remove_entity(self, entity: BaseClass) -> None:
        pass

    def calculate_strength(self) -> float:
        pass

    def get_entities_by_type(self, entity_type: str) -> List[BaseClass]:
        pass

    def update_metadata(self) -> None:
        pass
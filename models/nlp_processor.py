from typing import List, Set


class NLPProcessor:
    def __init__(self, min_word_frequency: int = 5, stop_words: Set[str] = None):
        self.min_word_frequency = min_word_frequency
        self.stop_words = stop_words or set()

    def calculate_high_frequency_words(self, text: str) -> List[str]:
        pass

    def calculate_unique_words(self, text: str) -> List[str]:
        pass

    def determine_theme(self, text: str) -> str:
        pass
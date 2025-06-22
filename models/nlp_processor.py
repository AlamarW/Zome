from typing import List, Set
import string
# from gensim import corpora, models
# from gensim.utils import simple_preprocess


class NLPProcessor:
    with open("stop_words_english.txt", "r") as f:
        _stop_words = set(word.strip().lower() for word in f)

    def __init__(self):
        pass

    def text_clean(text: str):
        if isinstance(text, str):
            text_clean = text.translate(str.maketrans("", "", string.punctuation))
        return text_clean

    def calculate_high_frequency_words(text: str) -> List[str]:
        words = text.lower().split()
        non_trivial_words = [w for w in words if w not in NLPProcessor._stop_words]
        print(non_trivial_words)
        word_count = {}

        # stemming words and counting
        for word in non_trivial_words:
            if len(word) > 1:
                root_word = word
                if word.endswith("ing") and len(word) > 4:
                    root_word = word[:-3]
                elif word.endswith("ed") and len(word) > 4:
                    root_word = word[:-2]

                word_count[root_word] = word_count.get(root_word, 0) + 1

        frequent_words = {}
        for word, count in word_count.items():
            if count > 1:
                frequent_words[word] = count

        # Sort by frequency (descending), then alphabetically
        sorted_words = dict(sorted(frequent_words.items(), key=lambda x: (-x[1], x[0])))
        return sorted_words

    def calculate_unique_words(self, text: str) -> List[str]:
        pass

    def determine_theme(self, text: str) -> str:
        pass


from typing import List, Dict, TYPE_CHECKING
import re
from gensim import corpora, models
from gensim.utils import simple_preprocess
from .base_class import BaseClass
from .nlp_processor import NLPProcessor

if TYPE_CHECKING:
    from .tag import Tag
    from .source_note import SourceNote
    from .attachment import Attachment
    from .draft import Draft


class Note(BaseClass):
    def __init__(self):
        super().__init__()
        self.name: str = ""
        self.text: str = ""
        self.high_frequency_words: Dict[str, int] = {}
        self.unique_words: List[str] = []  # words that are uncommon
        self.theme: List[str] = []
        self.source: List["SourceNote"] = []
        self.attachment: List["Attachment"] = []
        self.draft: List["Draft"] = []

    @staticmethod
    def _split_into_sentences(text: str) -> List[str]:
        """Split text into sentences using regex pattern"""
        if not text or not isinstance(text, str):
            return []

        # Pattern for sentence boundaries - periods, exclamation marks, question marks
        # followed by whitespace and capital letter, or end of string
        sentence_pattern = r"[.!?]+\s+(?=[A-Z])|[.!?]+$"

        # Split and clean sentences
        sentences = re.split(sentence_pattern, text.strip())

        # Filter out empty sentences and strip whitespace
        sentences = [s.strip() for s in sentences if s.strip()]

        return sentences

    def set_name(self, name: str) -> None:
        if not isinstance(name, str):
            self.name = (False, "Note.name must be a string")
        elif re.match(r"^[a-zA-Z0-9 .\-?!']+$", name):
            self.name = name
        else:
            self.name = (
                False,
                "Name can only include numbers letters, spaces, dashes (-), and regular punctuation",
            )

    def get_name(self) -> str:
        return self.name

    def set_text(self, text: str = "") -> None:
        if not isinstance(text, str):
            self.text = (False, "Note must be a string")
        else:
            self.text = text
            self._set_high_frequency_words()
            self.set_theme()

    def get_text(self) -> str:
        return self.text

    def get_high_frequency_words(self) -> Dict[str, int]:
        return self.high_frequency_words

    def _set_high_frequency_words(self) -> Dict[str, int]:
        if not self.text or not isinstance(self.text, str):
            return self.high_frequency_words

        # Basic stop words
        clean_text = NLPProcessor.text_clean(self.text)
        hfw = NLPProcessor.calculate_high_frequency_words(clean_text)
        self.high_frequency_words = hfw
        return self.high_frequency_words

    def get_themes(self) -> str:
        pass

    def set_theme(self) -> None:
        if not self.text or not isinstance(self.text, str):
            self.theme = []
            return

        # Split text into sentences for sentence-level topic modeling
        sentences = self._split_into_sentences(self.text)

        # If no sentences or only one very short sentence, fallback to word-level
        if len(sentences) == 0:
            self.theme = []
            return
        elif len(sentences) == 1 and len(sentences[0].split()) < 5:
            # Single short sentence - just use filtered words
            processed_text = simple_preprocess(sentences[0], deacc=True)
            if NLPProcessor._stop_words is None:
                self._get_stop_words()
            filtered_tokens = [
                token
                for token in processed_text
                if token not in NLPProcessor._stop_words and len(token) > 2
            ]
            self.theme = filtered_tokens[:3] if filtered_tokens else []
            return

        # Preprocess each sentence
        if NLPProcessor._stop_words is None:
            self._get_stop_words()

        processed_sentences = []
        for sentence in sentences:
            tokens = simple_preprocess(sentence, deacc=True)
            filtered_tokens = [
                token
                for token in tokens
                if token not in NLPProcessor._stop_words and len(token) > 2
            ]
            if (
                len(filtered_tokens) >= 2
            ):  # Only include sentences with at least 2 meaningful words
                processed_sentences.append(filtered_tokens)

        # Need at least 2 sentences with meaningful content for sentence-level LDA
        if len(processed_sentences) < 2:
            # Fallback to word-level approach for single sentence
            all_tokens = []
            for sentence in processed_sentences:
                all_tokens.extend(sentence)
            self.theme = all_tokens[:3] if all_tokens else []
            return

        # Create dictionary and corpus for sentence-level topic modeling
        dictionary = corpora.Dictionary(processed_sentences)
        corpus = [dictionary.doc2bow(sentence) for sentence in processed_sentences]

        # Use LDA with 1-3 topics based on number of sentences
        num_topics = min(3, max(1, len(processed_sentences) // 2))

        try:
            lda_model = models.LdaModel(
                corpus=corpus,
                id2word=dictionary,
                num_topics=num_topics,
                random_state=42,
                passes=10,
                alpha="auto",
                per_word_topics=True,
            )

            # Get the most probable topic and extract top words
            topic_words = []
            for topic_id in range(num_topics):
                words = lda_model.show_topic(topic_id, topn=3)
                topic_words.extend([word for word, _ in words])

            # Remove duplicates while preserving order
            unique_topic_words = []
            seen = set()
            for word in topic_words:
                if word not in seen:
                    unique_topic_words.append(word)
                    seen.add(word)

            self.theme = unique_topic_words[:5]  # Limit to 5 words max

        except Exception:
            # Fallback to most frequent words if topic modeling fails
            frequent_words = list(self.high_frequency_words.keys())[:3]
            self.theme = frequent_words if frequent_words else []

    def get_source(self) -> List["SourceNote"]:
        pass

    def set_source(self, source: List["SourceNote"]) -> None:
        pass

    def get_attachment(self) -> List["Attachment"]:
        pass

    def set_attachment(self, attachment: List["Attachment"]) -> None:
        pass

    def get_draft(self) -> List["Draft"]:
        pass

    def set_draft(self, draft: List["Draft"]) -> None:
        pass

    def find_similar_notes(self, notes: List["Note"]) -> List["Note"]:
        pass

    def get_notes_by_theme(self, theme: str, notes: List["Note"]) -> List["Note"]:
        pass

    def find_connections_by_words(self, notes: List["Note"]) -> List["Note"]:
        pass

    def update_nlp_data(self) -> None:
        pass

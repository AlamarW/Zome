import re
from typing import TextIO, ClassVar 
import string
from gensim import corpora # type: ignore
from gensim import models # type: ignore
from gensim.utils import simple_preprocess # type: ignore[import]

class NLPProcessor:
    _f: ClassVar[TextIO]
    with open("stop_words_english.txt", "r") as _f:
        _stop_words: set[str] = set(word.strip().lower() for word in _f)

    def __init__(self):
        pass

    @staticmethod
    def text_clean(text: str):
        if isinstance(text, str):
            text_clean = text.translate(str.maketrans("", "", string.punctuation))
        return text_clean

    @staticmethod
    def split_into_sentences(text: str) -> list[str]:
        """Split text into sentences using regex pattern"""
        if not text or not isinstance(text, str):
            return []

        # Pattern for sentence boundaries - periods, exclamation marks, question marks
        # followed by whitespace and capital letter, or end of string
        sentence_pattern = r"[.!?]+\s+(?=[A-Z])|[.!?]+$"

        sentences = re.split(sentence_pattern, text.strip())

        sentences = [s.strip() for s in sentences if s.strip()]

        return sentences

    @staticmethod
    def calculate_high_frequency_words(text: str) -> dict[str, int]:
        words = text.lower().split()
        non_trivial_words = [w for w in words if w not in NLPProcessor._stop_words]
        word_count: dict[str, int] = {}

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
        sorted_words: dict[str, int] = dict(sorted(frequent_words.items(), key=lambda x: (-x[1], x[0])))
        return sorted_words

    @staticmethod
    def determine_themes(text: str) -> list[str]:
        sentences = NLPProcessor.split_into_sentences(text)

        # If no sentences or only one very short sentence, fallback to word-level
        if len(sentences) == 0:
            theme: list[str] = []
            return theme
        elif len(sentences) == 1 and len(sentences[0].split()) < 5:
            # Single short sentence - just use filtered words
            processed_text = simple_preprocess(sentences[0], deacc=True)
            filtered_tokens: list[str] = [
                token
                for token in processed_text
                if token not in NLPProcessor._stop_words and len(token) > 2
            ]
            theme = filtered_tokens[:3] if filtered_tokens else []
            return theme

        processed_sentences: list[list[str]] = [] # each sentence becomes a list[str]
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
            all_tokens:list[str] = []
            for s in processed_sentences:
                all_tokens.extend(s)
            theme = all_tokens[:3] if all_tokens else []
            return theme

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
            topic_words:list[str] = []
            for topic_id in range(num_topics):
                words = lda_model.show_topic(topic_id, topn=3) 
                topic_words.extend([word for word, _ in words])

            # Remove duplicates while preserving order
            unique_topic_words:list[str] = []
            seen:set[str] = set()
            for word in topic_words:
                if word not in seen:
                    unique_topic_words.append(word)
                    seen.add(word)

            theme = unique_topic_words[:5]  # Limit to 5 words max
            return theme

        except Exception:
            # Fallback to most frequent words if topic modeling fails
            frequent_words = NLPProcessor.calculate_high_frequency_words(text)
            theme = list(frequent_words.keys())[:3] if frequent_words else []
            return theme

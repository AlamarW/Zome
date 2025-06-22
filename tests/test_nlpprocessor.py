import pytest

from models.nlp_processor import NLPProcessor


def test_get_stop_words():
    processor = NLPProcessor()

    assert len(processor._stop_words) == 850

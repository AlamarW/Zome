from garden.domain_models.nlp_processor import NLPProcessor


def test_get_stop_words():
    processor = NLPProcessor()

    assert len(processor._stop_words) == 850


def test_celan_text():
    text = "Testing, test but this is fine. Fine."

    clean_text = NLPProcessor.text_clean(text)

    assert clean_text == "Testing test but this is fine Fine"


def test_calculate_high_frequency_words():
    text = "Testing test but this is fine Fine"
    assert NLPProcessor.calculate_high_frequency_words(text) == {
        "test": 2,
        "fine": 2,
    }  # returns most frequent used words, minus stop words

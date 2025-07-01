import pytest

from garden.domain_models.note import Note


def test_set_name():
    note = Note()
    note.set_name("Bob")
    assert note.get_name() == "Bob"


def test_set_name_numbers_spaces():
    note = Note()
    note.set_name("Bob 1 sdf")
    assert note.get_name() == "Bob 1 sdf"


def test_set_forbidden_chars():
    note = Note()
    with pytest.raises(ValueError):
        note.set_name(
            "@#$"
        )  # names should only be alnum() space, dash, period, and question mark


def test_set_name_valid():
    note = Note()
    note.set_name("Wow! There's some weird stuff going on?")

    assert note.get_name() == "Wow! There's some weird stuff going on?"


def test_set_name_not_string():
    note = Note()
    with pytest.raises(TypeError):
        note.set_name(1234)


def test_set_text_empty():
    note = Note()
    note.set_text()

    assert note.get_text() == ""


def test_set_text_valid_note():
    note = Note()
    note.set_text(
        "This is a valid note, which can express multiple paragrpahs of information. This is just a simple example but serves for a much more, longer idea!"
    )

    assert (
        note.get_text()
        == "This is a valid note, which can express multiple paragrpahs of information. This is just a simple example but serves for a much more, longer idea!"
    )


def test_set_text_invalid_note():
    note = Note()

    with pytest.raises(TypeError):
        note.set_text(123)


def test_set_high_frequency_words():
    note = Note()
    note.set_text("Testing, test but this is fine. Fine.")
    print(note.get_high_frequency_words())
    assert note.get_high_frequency_words() == {
        "test": 2,
        "fine": 2,
    }  # returns most frequent used words, minus stop words


def test_set_themes_basic():
    note = Note()
    note.set_text(
        "Machine learning and artificial intelligence are transforming technology. Data science uses algorithms to analyze patterns in large datasets. Machine learning models require extensive training data to perform well."
    )

    # Theme should contain relevant topic words
    themes = note.themes
    assert isinstance(themes, list)
    assert len(themes) > 0
    # Should contain words related to the topic
    themes_lower = [word.lower() for word in themes]
    relevant_words = [
        "machine",
        "learning",
        "data",
        "science",
        "algorithm",
        "technology",
        "training",
        "models",
    ]
    # With sentence-level LDA, expect at least one relevant word
    assert any(word in themes_lower for word in relevant_words)


def test_set_themes_short_text():
    note = Note()
    note.set_text("Simple short note.")

    # For short text, should fallback to available words
    themes = note.themes
    assert isinstance(themes, list)
    # With sentence-level LDA, very short text might not generate topics
    # Should either be empty or contain meaningful words
    if themes:
        themes_lower = [word.lower() for word in themes]
        assert (
            "simple" in themes_lower
            or "short" in themes_lower
            or "note" in themes_lower
        )


def test_set_themes_empty_text():
    note = Note()
    note.set_text("")

    # Empty text should result in empty theme
    assert note.themes == []


def test_set_themes_multiple_sentences():
    note = Note()
    note.set_text(
        "Python is a programming language. It is used for data analysis and machine learning. "
        "Scientists love Python for its simplicity. Data scientists use Python libraries extensively."
    )

    # With multiple sentences, sentence-level LDA should find coherent topics
    theme = note.themes
    assert isinstance(theme, list)
    assert len(theme) > 0

    themes_lower = [word.lower() for word in theme]
    # Should capture the main topic (Python/programming/data)
    relevant_words = [
        "python",
        "data",
        "programming",
        "scientists",
        "analysis",
        "machine",
        "learning",
    ]
    assert any(word in themes_lower for word in relevant_words)


def test_set_themes_single_sentence():
    note = Note()
    note.set_text("Artificial intelligence transforms modern computing.")

    # Single sentence should still work but may have limited topic modeling
    theme = note.themes
    assert isinstance(theme, list)
    # Either empty (if too short for sentence-level) or contains relevant words
    if theme:
        themes_lower = [word.lower() for word in theme]
        relevant_words = ["artificial", "intelligence", "computing", "modern"]
        assert any(word in themes_lower for word in relevant_words)

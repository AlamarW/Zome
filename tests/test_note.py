import pytest

from models.note import Note


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
    note.set_name(
        "@#$"
    )  # names should only be alnum() space, dash, period, and question mark
    assert note.get_name() == (
        False,
        "Name can only include numbers letters, spaces, dashes (-), and regular punctuation",
    )


def test_set_name_valid():
    note = Note()
    note.set_name("Wow! There's some weird stuff going on?")

    assert note.get_name() == "Wow! There's some weird stuff going on?"


def test_set_name_not_string():
    note = Note()
    note.set_name(1234)

    assert note.get_name() == (False, "Note.name must be a string")


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
    note.set_text(123)

    assert note.get_text() == (False, "Note must be a string")


def test_set_high_frequency_words():
    note = Note()
    note.set_text("Testing, test but this is fine. Fine.")

    assert note.get_high_frequency_words() == {
        "test": 2,
        "fine": 2,
    }  # returns most frequent used words, minus stop words

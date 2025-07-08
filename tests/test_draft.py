import pytest
from garden.domain_models.draft import Draft

def test_set_name():
    d = Draft()

    d.set_name("A Compelling Title")

    assert d.get_name() == "A Compelling Title"

def test_set_text():
    d = Draft()

    d.set_text("Sample Text from an essay. These strings can be long and highly formatted")

    assert d.get_text() == "Sample Text from an essay. These strings can be long and highly formatted"

def test_set_type():
    d = Draft()

    d.set_type("Essay")

    assert d.get_type() == "Essay"

def test_set_type_only_allowed_value():
    d = Draft()

    d.set_type("InvalidValue")

    assert d.get_type() == ""

def test_show_allowed_types():

    assert Draft.show_allowed_types() == {"essay", "article", "story", "novel", "journal"}

def test_add_allowed_type():
    Draft._add_allowed_type("Column")

    assert Draft.show_allowed_types() == {"essay", "article", "story", "novel", "journal", "column"}


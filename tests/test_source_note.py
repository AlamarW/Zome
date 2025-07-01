import pytest
from garden.domain_models.source_note import SourceNote

#Testing inheritance works as expected
def test_set_text():
    sn = SourceNote()
    sn.set_text("Text to Demonstrate inheritance from note")

    assert sn.get_text() == "Text to Demonstrate inheritance from note"


#Testing methods native to SourceNote
def test_set_author():
    sn = SourceNote()
    sn.set_author("Valid Authorname")

    assert sn.get_author() == "Valid Authorname"

def test_set_author_name_is_string():
    sn = SourceNote()
    
    with pytest.raises(TypeError):
        sn.set_author(123)

def test_set_source_name():
    sn = SourceNote()
    sn.set_name("Test")

    assert sn.get_name() == "Test"

def test_get_source_type():
    sn = SourceNote()
    sn.set_source_type("Book")

    assert sn.get_source_type() == "book"

def test_current_types():
    for t in SourceNote._current_types:
        assert t in {"book", "video", "magazine", "newspaper", "article", "lecture"}

def test_set_source_type_not_in_current_type():
    sn = SourceNote()

    sn.set_source_type("Conference")

    assert sn.get_source_type() == "conference"
    assert "conference" in SourceNote._current_types

def test_set_source_type_invalid_value():
    sn = SourceNote()

    with pytest.raises(TypeError):
        sn.set_source_type(1234)

def test_set_source_type_same_with_space():
    sn = SourceNote()
    sn.set_source_type("   Book   ") #Has spaces

    assert sn.get_source_type() == "book"


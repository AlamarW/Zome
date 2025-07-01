import pytest
from garden.domain_models.source_note import SourceNote

def test_set_source_note():
    sn = SourceNote()
    sn.set_source_notes("This note has content in it")
    
    assert sn.get_source_notes() == "This note has content in it"

def test_set_source_note_invalid():
    sn = SourceNote()
    
    with pytest.raises(TypeError):
        sn.set_source_notes(123)

def test_set_author():
    sn = SourceNote()
    sn.set_author("Valid Authorname")

    assert sn.get_author() == "Valid Authorname"

def test_set_author_name_is_string():
    sn = SourceNote()
    
    with pytest.raises(TypeError):
        sn.set_author(123)


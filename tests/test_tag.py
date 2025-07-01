import pytest
from garden.domain_models.tag import Tag

def test_tag_name():
    t = Tag()
    t.set_tag_name("#TagName")

    assert t.get_tag_name() == "#TagName"

def test_tag_name_no_hash():
    t = Tag()
    t.set_tag_name("TagNoHash")

    assert t.get_tag_name() == "#TagNoHash"

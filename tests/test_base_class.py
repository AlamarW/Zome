from garden.domain_models.base_class import BaseClass
import uuid
import pytest

def test_set_tags():
    base = BaseClass()

    base.set_tags("#Test #Tags")

    assert base.tags == {"#Test", "#Tags"}

def test_set_tags_w_formatting():
    base = BaseClass()

    base.set_tags("#Test Not formatted correctlY")

    assert base.tags == {"#Test", "#Not", "#Formatted", "#Correctly"}

def test_set_tags_w_snake_case():
    base = BaseClass()

    base.set_tags("#Snake_case_tag #Another_Snake_Case_Tag")

    assert base.tags == {"#Snake_Case_Tag", "#Another_Snake_Case_Tag"}

def test_add_tag():
    base = BaseClass()
    base.set_tags("#Existing #Tags")

    base.add_tag("New_tag")

    assert base.tags == {"#Existing", "#Tags", "#New_Tag"}

def test_add_tag_not_correct_type():
    base = BaseClass()

    with pytest.raises(TypeError):
        base.set_tags(1234)

def test_remove_tag():
    base = BaseClass()
    base.set_tags("#Not_This_One #This_One")

    base.remove_tag("#This_One")

    assert base.tags == {"#Not_This_One"}

def test_remove_tag_not_formatted():
    base = BaseClass()
    base.set_tags("#Not_This_One #This_One")

    base.remove_tag("This_One")

    assert base.tags == {"#Not_This_One"}

def test_remove_tag_invalid_type():
    base = BaseClass()
    base.set_tags("#Tags_To_Have #Tags2")

    with pytest.raises(TypeError):
        base.remove_tag(1234)

def test_compare_equal_tags():
    base1 = BaseClass()
    base2 = BaseClass()
    base1.set_tags("#Tag_To_Compare")
    base2.set_tags("#Tag_To_Compare")

    assert base1.compare_equal_tags(base2) == True



def test_set_uuid():
    base = BaseClass()

    assert isinstance(base.uuid, uuid.UUID)

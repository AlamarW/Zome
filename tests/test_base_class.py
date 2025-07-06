from garden.domain_models.base_class import BaseClass


def test_set_tags():
    base = BaseClass()

    base.set_tags("#Test #Tags")

    assert base.tags == ["#Test", "#Tags"]

def test_set_tags_w_formatting():
    base = BaseClass()

    base.set_tags("#Test Not formatted correctlY")

    assert base.tags == ["#Test", "#Not", "#Formatted", "#Correctly"]

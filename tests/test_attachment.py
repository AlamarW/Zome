import pytest
from garden.domain_models.attachment import Attachment

def test_set_attachemnt():
    a = Attachment()

    a.set_attachment("test/path/file")

    assert a.attachment == "test/path/file"

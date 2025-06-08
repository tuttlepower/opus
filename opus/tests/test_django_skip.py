import pytest

pytest.importorskip('django')
from django.conf import settings


def test_django_settings():
    assert settings.configured

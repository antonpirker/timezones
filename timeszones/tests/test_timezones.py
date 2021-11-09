import os
import tempfile

import pytest

from .. import timezones


@pytest.fixture
def client():
    timezones.app.config["TESTING"] = True

    with timezones.app.test_client() as client:
        yield client


def test_root(client):
    """Test API root"""

    response = client.get("/")
    assert b'{"timezones":"http://localhost/timezones"}' in response.data

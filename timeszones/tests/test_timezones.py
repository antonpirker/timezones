import os
import tempfile

import pytest

from .. import timezones


@pytest.fixture
def client():
    timezones.app.config["TESTING"] = True

    with timezones.app.test_client() as client:
        yield client


def test_something(client):
    """Test for something"""

    response = client.get("/")
    print(response)
    assert b"xxx" in response.data

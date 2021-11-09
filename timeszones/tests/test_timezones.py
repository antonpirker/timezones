import os
import tempfile

import pytest
import json

from .. import timezones

TOTAL_TIMEZONES = 413


@pytest.fixture
def client():
    timezones.app.config["TESTING"] = True

    with timezones.app.test_client() as client:
        yield client


def test_root(client):
    """Test API root"""

    rv = client.get("/")
    assert b'{"timezones":"http://localhost/timezones"}' in rv.data


def test_timezone_list(client):
    """If lat/lon is NOT given a list of all timezones is returned"""
    rv = client.get("/timezones")
    data = json.loads(rv.data)

    assert "timezones" in data.keys()
    assert len(data["timezones"]) == TOTAL_TIMEZONES


def test_timezone(client):
    """If lat/lon is given, a timezone name is returned"""
    rv = client.get("/timezones?lat=48.19&lon=16.39")
    data = json.loads(rv.data)

    assert "timezone" in data
    assert data["timezone"] == "Europe/Vienna"


def test_uninhabitated_timezone(client):
    """If lat/lon is uninhabitated the timezone is UTC"""
    rv = client.get("/timezones?lat=0&lon=0")
    data = json.loads(rv.data)

    assert "timezone" in data
    assert data["timezone"] == "UTC"

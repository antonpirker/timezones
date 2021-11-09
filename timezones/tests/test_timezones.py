import pytest

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
    data = rv.get_json()

    assert "timezones" in data.keys()
    assert len(data["timezones"]) == TOTAL_TIMEZONES
    assert data["timezones"][0] == "Africa/Abidjan"
    assert data["timezones"][-1] == "uninhabited"


def test_timezone(client):
    """If lat/lon is given, a timezone name is returned"""
    rv = client.get("/timezones?lat=48.19&lon=16.39")
    data = rv.get_json()

    assert "timezone" in data
    assert data["timezone"] == "Europe/Vienna"


def test_uninhabitated_timezone(client):
    """If lat/lon is uninhabitated the timezone is UTC"""
    rv = client.get("/timezones?lat=0&lon=0")
    data = rv.get_json()

    assert "timezone" in data
    assert data["timezone"] == "UTC"


def test_bad_requests(client):
    """Test bad requests"""
    rv = client.get("/timezones?lat=48.19")
    assert rv.status == "400 BAD REQUEST"

    rv = client.get("/timezones?lon=16.39")
    assert rv.status == "400 BAD REQUEST"

    rv = client.get("/timezones?lat=48.19&lon=999999")
    assert rv.status == "400 BAD REQUEST"

    rv = client.get("/timezones?lat=999999&lon=16.39")
    assert rv.status == "400 BAD REQUEST"

    rv = client.get("/timezones?lat=48.19&lon=-999999")
    assert rv.status == "400 BAD REQUEST"

    rv = client.get("/timezones?lat=-999999&lon=16.39")
    assert rv.status == "400 BAD REQUEST"

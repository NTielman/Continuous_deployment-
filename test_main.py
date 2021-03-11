import pytest
from datetime import date, timedelta

from main import app
today = date.today()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_index(client):
    response = client.get('/')

    assert response.status_code == 200
    assert f'Today is {today.isoformat()}'.encode(
        'utf-8') in response.data


def test_redirect(client):
    response = client.get('/today/')

    assert response.status_code == 302


def test_days(client):
    response = client.get('/tomorrow/')

    assert response.status_code == 200
    assert f'Tomorrow is {tomorrow.isoformat()}'.encode(
        'utf-8') in response.data

    response = client.get('/yesterday/')

    assert response.status_code == 200
    assert f'Yesterday was {yesterday.isoformat()}'.encode(
        'utf-8') in response.data

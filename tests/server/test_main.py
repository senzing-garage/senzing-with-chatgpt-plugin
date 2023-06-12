import pytest
from fastapi.testclient import TestClient

from server.main import app

from .constants import (
    ENTITY_1,
    ENTITY_HOW_1,
    EXPORT_MATCHED_LIMIT10,
    EXPORT_POSSIBLE_MATCHES_LIMIT10,
    EXPORT_POSSIBLE_RELATIONSHIPS_LIMIT10,
    SEARCH_NAME_FULL_BOB_SMITH,
)


@pytest.fixture
def client():
    return TestClient(app)

#
# Export
#
# https://docs.senzing.com/python/3/g2engine/reporting/index.html#exportjsonentityreport
def test_entity_report_matched(client):
    resp = client.get('/entity_report?export_flags=MATCHED')
    assert 200 == resp.status_code
    assert resp.json() == EXPORT_MATCHED_LIMIT10

def test_entity_report_possible_matches(client):
    resp = client.get('/entity_report?export_flags=POSSIBLE_MATCHES')
    assert 200 == resp.status_code
    assert resp.json() == EXPORT_POSSIBLE_MATCHES_LIMIT10

def test_entity_report_possible_relationships(client):
    resp = client.get('/entity_report?export_flags=POSSIBLE_RELATIONSHIPS')
    assert 200 == resp.status_code
    assert resp.json() == EXPORT_POSSIBLE_RELATIONSHIPS_LIMIT10

#
# Entity Details
#
# https://docs.senzing.com/python/3/g2engine/getting/index.html#getentitybyentityid
def test_entity_details(client):
    resp = client.get('/entity_details?entity_id=1')
    assert 200 == resp.status_code
    assert resp.json() == ENTITY_1

#
# Entity How
#
# https://docs.senzing.com/python/3/g2engine/how/index.html
def test_entity_how(client):
    resp = client.get('/entity_how?entity_id=1')
    assert 200 == resp.status_code
    assert resp.json() == ENTITY_HOW_1

#
# Search Attrs
#
# https://docs.senzing.com/python/3/g2engine/searching/index.html#searchbyattributes
def test_search(client):
    resp = client.post('/search', json=dict(NAME_FULL='Bob Smith'))
    assert 200 == resp.status_code
    assert resp.json() == SEARCH_NAME_FULL_BOB_SMITH


import pytest

from server import senzing_api
from server.senzing_api import SenzingAPI

from .constants import (
    ENTITY_1,
    ENTITY_HOW_1,
    EXPORT_MATCHED_LIMIT10,
    EXPORT_POSSIBLE_MATCHES_LIMIT10,
    EXPORT_POSSIBLE_RELATIONSHIPS_LIMIT10,
    RECORD_1001,
    SEARCH_NAME_FULL_BOB_SMITH,
)


@pytest.fixture
def api():
    return SenzingAPI()

class TestSenzingAPI:
    #
    # Export
    #
    # https://docs.senzing.com/python/3/g2engine/reporting/index.html#exportjsonentityreport
    def test_export_matched(self, api):
        results = api.export(senzing_api.EXPORT_FLAGS_MATCHED)
        assert results == EXPORT_MATCHED_LIMIT10

    def test_export_possible_matches(self, api):
        results = api.export(senzing_api.EXPORT_FLAGS_POSSIBLE_MATCHES)
        assert results == EXPORT_POSSIBLE_MATCHES_LIMIT10

    def test_export_possible_relationships(self, api):
        results = api.export(senzing_api.EXPORT_FLAGS_POSSIBLE_RELSHIPS)
        assert results == EXPORT_POSSIBLE_RELATIONSHIPS_LIMIT10

    #
    # Record
    #
    # https://docs.senzing.com/python/3/g2engine/getting/index.html#getrecord
    def test_record_get(self, api):
        result = api.record_get('CUSTOMERS', '1001')
        assert result == RECORD_1001

    #
    # Entity Details
    #
    # https://docs.senzing.com/python/3/g2engine/getting/index.html#getentitybyentityid
    def test_entity_details(self, api):
        result = api.entity_details(1)
        assert result == ENTITY_1

    #
    # Entity How
    #
    # https://docs.senzing.com/python/3/g2engine/how/index.html
    def test_entity_how(self, api):
        result = api.entity_how(1)
        assert result == ENTITY_HOW_1

    #
    # Search Attrs
    #
    # https://docs.senzing.com/python/3/g2engine/searching/index.html#searchbyattributes
    def test_search(self, api):
        results = api.search(dict(NAME_FULL='Bob Smith'))
        assert results == SEARCH_NAME_FULL_BOB_SMITH


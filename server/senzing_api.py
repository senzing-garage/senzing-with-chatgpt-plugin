import json
import os

from senzing import (
    G2Engine,
    G2EngineFlags,
    )

#
# Config
#
ENGINE_CONFIG = os.getenv('SENZING_ENGINE_CONFIGURATION_JSON', None)

EXPORT_LIMIT = 10

ENTITY_FLAGS                   = G2EngineFlags.G2_ENTITY_INCLUDE_RECORD_DATA \
                               | G2EngineFlags.G2_ENTITY_INCLUDE_RELATED_MATCHING_INFO \
                               | G2EngineFlags.G2_ENTITY_INCLUDE_ALL_RELATIONS \
                               | G2EngineFlags.G2_ENTITY_INCLUDE_ENTITY_NAME \
                               | G2EngineFlags.G2_ENTITY_INCLUDE_RELATED_ENTITY_NAME

EXPORT_FLAGS_MATCHED           = G2EngineFlags.G2_EXPORT_INCLUDE_RESOLVED
EXPORT_FLAGS_POSSIBLE_MATCHES  = G2EngineFlags.G2_EXPORT_INCLUDE_POSSIBLY_SAME
EXPORT_FLAGS_POSSIBLE_RELSHIPS = G2EngineFlags.G2_EXPORT_INCLUDE_POSSIBLY_RELATED

DETAILS_FLAGS                  = G2EngineFlags.G2_ENTITY_INCLUDE_REPRESENTATIVE_FEATURES

HOW_FLAGS                      = G2EngineFlags.G2_HOW_ENTITY_DEFAULT_FLAGS

#
# Senzing API
#
class SenzingAPI:
    def __init__(self):
        self._engine = None

    def __del__(self):
        if self._engine:
            self._engine.destroy()
            self._engine = None

    #
    # Engine
    #
    @property
    def engine(self):
        if not self._engine:
            self._engine = G2Engine()
            self._engine.init('G2Engine', ENGINE_CONFIG, False)
        return self._engine

    #
    # Export
    #
    # https://docs.senzing.com/python/3/g2engine/reporting/index.html#exportjsonentityreport
    def export(self, export_flags, limit=EXPORT_LIMIT):
        fetch_next_response = bytearray()

        export_handle = self.engine.exportJSONEntityReport(ENTITY_FLAGS | export_flags)

        export_results = []
        for _ in range(limit):
            record = self.engine.fetchNext(export_handle, fetch_next_response)
            if not record:
                break
            export_results.append(json.loads(record.decode()))

        self.engine.closeExport(export_handle)

        return export_results

    #
    # Record
    #
    # https://docs.senzing.com/python/3/g2engine/getting/index.html#getrecord
    def record_get(self, dsrc_code, record_id):
        response = bytearray()

        self.engine.getRecord(dsrc_code, record_id, response)
        record = json.loads(response.decode())

        return record

    #
    # Entity Details
    #
    # https://docs.senzing.com/python/3/g2engine/getting/index.html#getentitybyentityid
    def entity_details(self, entity_id):
        response = bytearray()

        self.engine.getEntityByEntityID(entity_id,
                                        response,
                                        ENTITY_FLAGS | DETAILS_FLAGS)
        entity = json.loads(response.decode())

        return entity

    #
    # Entity How
    #
    # https://docs.senzing.com/python/3/g2engine/how/index.html
    def entity_how(self, entity_id):
        response = bytearray()

        self.engine.howEntityByEntityID(entity_id, response, HOW_FLAGS)
        how = json.loads(response.decode())

        return how

    #
    # Search Attrs
    #
    # https://docs.senzing.com/python/3/g2engine/searching/index.html#searchbyattributes
    def search(self, attrs):
        response = bytearray()

        self.engine.searchByAttributes(json.dumps(attrs), response)
        results = json.loads(response.decode())

        return results


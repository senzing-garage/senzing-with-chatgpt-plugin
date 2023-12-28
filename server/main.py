import enum
import os
from typing import (
    Annotated,
    Optional,
)

import uvicorn
from fastapi import (
    Depends,
    FastAPI,
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_utils.enums import StrEnum
from pydantic import BaseModel

from server import senzing_api
from server.senzing_api import SenzingAPI

#
# Environment
#
env_development = 'dev' == os.getenv('ENV', 'dev')

#
# Senzing API
#
def api_create() -> SenzingAPI:
    return SenzingAPI()

#
# Models
#
class ExportFlags(StrEnum):
    MATCHED                = enum.auto()
    POSSIBLE_MATCHES       = enum.auto()
    POSSIBLE_RELATIONSHIPS = enum.auto()

EXPORT_FLAG_MAP = {
    ExportFlags.MATCHED:                senzing_api.EXPORT_FLAGS_MATCHED,
    ExportFlags.POSSIBLE_MATCHES:       senzing_api.EXPORT_FLAGS_POSSIBLE_MATCHES,
    ExportFlags.POSSIBLE_RELATIONSHIPS: senzing_api.EXPORT_FLAGS_POSSIBLE_RELSHIPS,
    }

# https://github.com/senzing-garage/senzing-rest-api-specification/blob/main/senzing-rest-api.yaml#L283
# https://raw.githubusercontent.com/Senzing/senzing-rest-api/master/senzing-rest-api.yaml
class SearchAttributes(BaseModel):
    NAME_ORG: Optional[str]
    NAME_FULL: Optional[str]
    NAME_LAST: Optional[str]
    NAME_FIRST: Optional[str]
    NAME_MIDDLE: Optional[str]
    NAME_SUFFIX: Optional[str]
    ADDR_FULL: Optional[str]
    ADDR_LINE1: Optional[str]
    ADDR_CITY: Optional[str]
    ADDR_STATE: Optional[str]
    ADDR_POSTAL_CODE: Optional[str]
    ADDR_COUNTRY: Optional[str]
    PHONE_NUMBER: Optional[str]
    EMAIL_ADDRESS: Optional[str]
    DATE_OF_BIRTH: Optional[str]
    DRIVERS_LICENSE_NUMBER: Optional[str]
    SSN_NUMBER: Optional[str]
    NATIONAL_ID_NUMBER: Optional[str]
    PASSPORT_NUMBER: Optional[str]
    PASSPORT_COUNTRY: Optional[str]

#
# App
#
app = FastAPI(
    title = 'Senzing Entity Resolution Plugin',
    version = '1.0.1',
    description = (
        'Senzing Conversational AI for Entity Resolution plugin '
        'that allows you to interact with entity resolution via natural language.'
        ),
    )

app.mount('/.well-known', StaticFiles(directory='.well-known'), name='static')

# Development: Allow Localhost
if env_development:
    origins = [
        'http://localhost:8080',
        'https://chat.openai.com',
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

#
# Export
#
# https://docs.senzing.com/python/3/g2engine/reporting/index.html#exportjsonentityreport
@app.get('/entity_report')
def entity_report(
    export_flags: ExportFlags,
    api: Annotated[SenzingAPI, Depends(api_create)],
) -> list:
    '''
    Return 10 entities with either matches, possible matches, or relationships.
    '''
    api_flags = EXPORT_FLAG_MAP[export_flags]
    return api.export(api_flags)

#
# Entity Details
#
# https://docs.senzing.com/python/3/g2engine/getting/index.html#getentitybyentityid
@app.get('/entity_details')
def entity_details(
    entity_id: int,
    api: Annotated[SenzingAPI, Depends(api_create)],
) -> dict:
    '''
    Retrieve entity data based on the ID of a resolved identity.
    '''
    return api.entity_details(entity_id)

#
# Entity How
#
# https://docs.senzing.com/python/3/g2engine/how/index.html
@app.get('/entity_how')
def entity_how(
    entity_id: int,
    api: Annotated[SenzingAPI, Depends(api_create)],
) -> dict:
    '''
    Determines and details steps-by-step how records resolved to an ENTITY_ID.
    '''
    return api.entity_how(entity_id)

#
# Search Attrs
#
# https://docs.senzing.com/python/3/g2engine/searching/index.html#searchbyattributes
@app.post('/entity_search')
def entity_search(
    attrs: SearchAttributes,
    api: Annotated[SenzingAPI, Depends(api_create)],
) -> dict:
    '''
    Retrieves entity data based on a user-specified set of entity attributes.
    '''
    attrs = attrs.dict(exclude_unset=True)
    return api.search(attrs)

#
# Start
#
def start():
    uvicorn.run('server.main:app', host='0.0.0.0', port=8080, reload=True)


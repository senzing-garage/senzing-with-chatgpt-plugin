"""Usage: openapi_schema.py
"""
import pathlib

import yaml
from fastapi.openapi.utils import get_openapi

from server.main import app


#
# OpenAPI Schema
#
def openapi_schema_generate():
    schema = get_openapi(title = app.title,
                         version = app.version,
                         openapi_version = app.openapi_version,
                         description = app.description,
                         routes = app.routes,
                         )
    return schema

#
# Main
#
def main():
    # Schema: Generate
    schema_file = pathlib.Path('.') / '.well-known' / 'openapi.yaml'
    schema = openapi_schema_generate()

    with open(schema_file, 'w') as f:
        yaml.dump(schema, f)

    print(f'Wrote: {schema_file}')

if '__main__' == __name__:
    main()


from server.openapi_schema import openapi_schema_generate


def test_openapi_schema_generate():
    _ = openapi_schema_generate()
    assert True # Just check that there are no input errors


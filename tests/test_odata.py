import pytest
from d365.odata import ODataClient

@pytest.fixture
def odata_client():
    client = ODataClient(client_id='your_client_id', client_secret='your_client_secret')
    yield client

def test_fetch_entities(odata_client):
    entity_name = 'YourEntityName'
    response = odata_client.fetch_entities(entity_name)
    assert response is not None
    assert isinstance(response, list)

def test_create_entity(odata_client):
    entity_name = 'YourEntityName'
    data = {'key': 'value'}
    response = odata_client.create_entity(entity_name, data)
    assert response is not None
    assert response.get('key') == 'value'
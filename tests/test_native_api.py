import pytest
from d365.native_api import NativeAPIClient

class TestNativeAPIClient:
    def setup_method(self):
        self.client = NativeAPIClient(client_id='test_client_id', client_secret='test_client_secret')

    def test_get_data(self):
        endpoint = 'test/endpoint'
        response = self.client.get_data(endpoint)
        assert response is not None  # Replace with actual expected response check

    def test_post_data(self):
        endpoint = 'test/endpoint'
        data = {'key': 'value'}
        response = self.client.post_data(endpoint, data)
        assert response is not None  # Replace with actual expected response check
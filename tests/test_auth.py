import pytest
from d365.auth import AuthManager

@pytest.fixture
def auth_manager():
    return AuthManager()

def test_get_access_token(auth_manager):
    client_id = "test_client_id"
    client_secret = "test_client_secret"
    token = auth_manager.get_access_token(client_id, client_secret)
    assert token is not None
    assert isinstance(token, str)

def test_store_token(auth_manager):
    token = "test_access_token"
    auth_manager.store_token(token)
    stored_token = auth_manager.get_stored_token()  # Assuming a method to retrieve the stored token
    assert stored_token == token
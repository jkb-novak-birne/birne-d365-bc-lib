import unittest
from unittest.mock import patch
from birneD365.bc import AuthManager
import time
import base64
import json

class TestAuthManager(unittest.TestCase):
    def setUp(self):
        self.auth_manager = AuthManager()
        self.client_id = "test_client_id"
        self.client_secret = "test_client_secret"

    @patch('requests.post')
    def test_get_access_token(self, mock_post):
        # Mock the response from the token endpoint
        mock_response = {
            "access_token": "test_access_token"
        }
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response

        token = self.auth_manager.get_access_token(self.client_id, self.client_secret, "test_tenant_id")
        self.assertEqual(token, "test_access_token")
        self.assertEqual(self.auth_manager.access_token, "test_access_token")

    def test_is_token_expired(self):
        # Create a token that expires in 1 second
        payload = {
            "exp": time.time() + 1
        }
        encoded_payload = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip('=')
        token = f"header.{encoded_payload}.signature"

        # Token should not be expired initially
        self.assertFalse(self.auth_manager.is_token_expired(token))

        # Wait for 2 seconds to ensure the token is expired
        time.sleep(2)

        # Token should be expired now
        self.assertTrue(self.auth_manager.is_token_expired(token))

    def test_is_token_expired_invalid_format(self):
        # Test with an invalid token format
        invalid_token = "invalid_base64_string=="
        self.assertTrue(self.auth_manager.is_token_expired(invalid_token))

    def test_is_token_expired_no_exp(self):
        # Create a token without an exp field
        payload = {}
        encoded_payload = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip('=')
        token = f"header.{encoded_payload}.signature"
        self.assertTrue(self.auth_manager.is_token_expired(token))

    def test_is_token_valid(self):
        # Create a valid token
        payload = {
            "exp": time.time() + 60  # Expires in 60 seconds
        }
        encoded_payload = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip('=')
        token = f"header.{encoded_payload}.signature"
        self.auth_manager.store_token(token)

        # Token should be valid
        self.assertTrue(self.auth_manager.is_token_valid())

        # Create an expired token
        payload = {
            "exp": time.time() - 60  # Expired 60 seconds ago
        }
        encoded_payload = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip('=')
        expired_token = f"header.{encoded_payload}.signature"
        self.auth_manager.store_token(expired_token)

        # Token should be invalid
        self.assertFalse(self.auth_manager.is_token_valid())

if __name__ == '__main__':
    unittest.main()
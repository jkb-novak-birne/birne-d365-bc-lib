import requests
import base64
import json
import time

class AuthManager:
    def __init__(self):
        self.access_token = None

    def get_access_token(self, client_id, client_secret, tenant_id):
        url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
            "scope": "https://api.businesscentral.dynamics.com/.default"
        }
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        self.access_token = response.json().get("access_token")
        return self.access_token

    def store_token(self, token):
        self.access_token = token

    def is_token_valid(self):
        return self.access_token is not None and not self.is_token_expired(self.access_token)

    def is_token_expired(self, token):
        # Decode the JWT token to get the expiration time
        token_parts = token.split('.')
        if len(token_parts) != 3:
            return True  # Invalid token format

        payload = token_parts[1]
        # Add padding if necessary
        payload += '=' * (4 - len(payload) % 4)
        decoded_payload = base64.urlsafe_b64decode(payload)
        payload_json = json.loads(decoded_payload)

        exp = payload_json.get('exp')
        if exp is None:
            return True  # No expiration time in token

        current_time = time.time()
        return current_time > exp
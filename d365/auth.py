class AuthManager:
    def __init__(self):
        self.access_token = None

    def get_access_token(self, client_id, client_secret):
        # Logic to obtain access token from D365 Business Central API
        # This typically involves making a POST request to the token endpoint
        # with the client_id and client_secret.
        pass

    def store_token(self, token):
        # Logic to securely store the access token
        self.access_token = token

    def is_token_valid(self):
        # Logic to check if the access token is still valid
        return self.access_token is not None and not self.is_token_expired(self.access_token)

    def is_token_expired(self, token):
        # Logic to determine if the token is expired
        pass
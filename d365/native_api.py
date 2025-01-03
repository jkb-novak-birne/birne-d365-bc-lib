class NativeAPIClient:
    def __init__(self, auth_manager):
        self.auth_manager = auth_manager

    def get_data(self, endpoint):
        token = self.auth_manager.get_access_token()
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        return response.json()

    def post_data(self, endpoint, data):
        token = self.auth_manager.get_access_token()
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        response = requests.post(endpoint, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
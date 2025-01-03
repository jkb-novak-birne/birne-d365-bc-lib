class ODataClient:
    def __init__(self, base_url, auth_manager):
        self.base_url = base_url
        self.auth_manager = auth_manager

    def fetch_entities(self, entity_name):
        access_token = self.auth_manager.get_access_token()
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        response = requests.get(f'{self.base_url}/{entity_name}', headers=headers)
        response.raise_for_status()
        return response.json()

    def create_entity(self, entity_name, data):
        access_token = self.auth_manager.get_access_token()
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        response = requests.post(f'{self.base_url}/{entity_name}', json=data, headers=headers)
        response.raise_for_status()
        return response.json()
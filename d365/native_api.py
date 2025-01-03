import requests
from d365.auth import AuthManager

class NativeAPI:
    def __init__(self, auth_manager, tenant_id, company_id, env_name):
        self.auth_manager = auth_manager
        self.tenant_id = tenant_id
        self.company_id = company_id
        self.env_name = env_name
        self.base_url = f"https://api.businesscentral.dynamics.com/v2.0/{tenant_id}/{env_name}/api/v2.0/companies({company_id})"

    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.auth_manager.access_token}",
            "Content-Type": "application/json"
        }

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        headers = self.get_headers()
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
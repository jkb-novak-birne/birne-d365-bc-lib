from d365.auth import AuthManager
from d365.native_api import NativeAPI
from d365.odata import ODataAPI

class D365Wrapper:
    def __init__(self, client_id, client_secret, tenant_id, company_id, env_name):
        self.auth_manager = AuthManager()
        self.auth_manager.get_access_token(client_id, client_secret, tenant_id)
        self.native_api = NativeAPI(self.auth_manager, tenant_id, company_id, env_name)
        self.odata_api = ODataAPI(self.auth_manager, tenant_id, company_id, env_name)

    def get_native(self, endpoint):
        return self.native_api.get(endpoint)

    def post_native(self, endpoint, data):
        return self.native_api.post(endpoint, data)

    def get_odata(self, endpoint):
        return self.odata_api.get(endpoint)

    def post_odata(self, endpoint, data):
        return self.odata_api.post(endpoint, data)
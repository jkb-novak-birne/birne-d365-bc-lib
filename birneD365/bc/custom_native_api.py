from .native_api import NativeAPI

class CustomNativeAPI(NativeAPI):
    def __init__(self, auth_manager, tenant_id, company_id, env_name):
        super().__init__(auth_manager, tenant_id, company_id, env_name)
        self.base_url = f"https://api.businesscentral.dynamics.com/v2.0/{env_name}/api/Soft4/Birne/v2.0/companies({company_id})"

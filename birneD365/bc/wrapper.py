import pandas as pd
from .auth import AuthManager
from .native_api import NativeAPI
from .odata import ODataAPI
from .custom_native_api import CustomNativeAPI

class D365Wrapper:
    def __init__(self, client_id, client_secret, tenant_id, company_id, env_name):
        self.auth_manager = AuthManager()
        self.auth_manager.get_access_token(client_id, client_secret, tenant_id)
        self.native_api = NativeAPI(self.auth_manager, tenant_id, company_id, env_name)
        self.odata_api = ODataAPI(self.auth_manager, tenant_id, company_id, env_name)
        self.custom_native_api = CustomNativeAPI(self.auth_manager, tenant_id, company_id, env_name)

    def get_native(self, endpoint, filters=None, orderby=None, maxpagesize=None):
        return self.native_api.get(endpoint, filters, orderby, maxpagesize)

    def get_all_native_pages(self, endpoint, filters=None, orderby=None, maxpagesize=None):
        return self.native_api.get_all_pages(endpoint, filters, orderby, maxpagesize)

    def get_odata(self, endpoint, filters=None, orderby=None, maxpagesize=None):
        return self.odata_api.get(endpoint, filters, orderby, maxpagesize)

    def get_all_odata_pages(self, endpoint, filters=None, orderby=None, maxpagesize=None):
        return self.odata_api.get_all_pages(endpoint, filters, orderby, maxpagesize)

    def get_native_as_dataframe(self, endpoint, filters=None, orderby=None, maxpagesize=None):
        data = self.get_native(endpoint, filters, orderby, maxpagesize)
        if "value" in data:
            data = data["value"]
        return pd.DataFrame(data)

    def get_all_native_pages_as_dataframe(self, endpoint, filters=None, orderby=None, maxpagesize=None):
        data = self.get_all_native_pages(endpoint, filters, orderby, maxpagesize)
        return pd.DataFrame(data)

    def get_odata_as_dataframe(self, endpoint, filters=None, orderby=None, maxpagesize=None):
        data = self.get_odata(endpoint, filters, orderby, maxpagesize)
        if "value" in data:
            data = data["value"]
        return pd.DataFrame(data)

    def get_all_odata_pages_as_dataframe(self, endpoint, filters=None, orderby=None, maxpagesize=None):
        data = self.get_all_odata_pages(endpoint, filters, orderby, maxpagesize)
        return pd.DataFrame(data)

    def get_custom_native(self, endpoint, filters=None, orderby=None, maxpagesize=None):
        return self.custom_native_api.get(endpoint, filters, orderby, maxpagesize)

    def get_all_custom_native_pages(self, endpoint, filters=None, orderby=None, maxpagesize=None):
        return self.custom_native_api.get_all_pages(endpoint, filters, orderby, maxpagesize)

    def get_custom_native_as_dataframe(self, endpoint, filters=None, orderby=None, maxpagesize=None):
        data = self.get_custom_native(endpoint, filters, orderby, maxpagesize)
        if "value" in data:
            data = data["value"]
        return pd.DataFrame(data)

    def get_all_custom_native_pages_as_dataframe(self, endpoint, filters=None, orderby=None, maxpagesize=None):
        data = self.get_all_custom_native_pages(endpoint, filters, orderby, maxpagesize)
        return pd.DataFrame(data)
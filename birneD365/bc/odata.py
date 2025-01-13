import requests

class ODataAPI:
    def __init__(self, auth_manager, tenant_id, company_id, env_name):
        self.auth_manager = auth_manager
        self.tenant_id = tenant_id
        self.company_id = company_id
        self.env_name = env_name
        self.base_url = f"https://api.businesscentral.dynamics.com/v2.0/{tenant_id}/{env_name}/ODataV4/Company('{company_id}')"

    def get_headers(self, maxpagesize=None):
        headers = {
            "Authorization": f"Bearer {self.auth_manager.access_token}",
            "Content-Type": "application/json"
        }
        if maxpagesize:
            headers["Prefer"] = f"odata.maxpagesize={str(maxpagesize)}"
        return headers

    def construct_query(self, filters=None, orderby=None):
        query_params = []
        if filters:
            query_params.append(f"$filter={filters}")
        if orderby:
            query_params.append(f"$orderby={orderby}")
        return "&".join(query_params)

    def get(self, endpoint, filters=None, orderby=None, maxpagesize=None):
        query_string = self.construct_query(filters, orderby)
        url = f"{self.base_url}/{endpoint}"
        if query_string:
            url = f"{url}?{query_string}"
        headers = self.get_headers(maxpagesize)
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_all_pages(self, endpoint, filters=None, orderby=None, maxpagesize=None):
        all_data = []
        next_link = None

        while True:
            data = self.get(endpoint, filters, orderby, maxpagesize)
            if "value" in data:
                all_data.extend(data["value"])
            else:
                all_data.extend(data)

            next_link = data.get("@odata.nextLink")
            if not next_link:
                break

            endpoint = next_link.replace(self.base_url + "/", "")
            #null filters as they are already in next link
            filters = None
        return all_data

    def post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        headers = self.get_headers()
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint, key_values):
        key_value_str = ",".join([f"{key}={value}" for key, value in key_values.items()])
        url = f"{self.base_url}/{endpoint}({key_value_str})"
        headers = self.get_headers()
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return response.status_code
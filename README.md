# D365 Business Central Library

A Python library for interacting with D365 Business Central using native API and OData protocol.

## Features

- **Authentication Management**: Handles OAuth2 authentication using client ID and client secret.
- **Native API Interaction**: Provides methods to interact with the native API for data retrieval and manipulation.
- **OData Protocol Support**: Allows fetching and creating entities using the OData protocol.
- **Utility Functions**: Includes helper functions for token management and configuration loading.

## Installation

To install the library, use pip:

```sh
pip install -r requirements.txt
```

Or install directly from the GitHub repository:

```sh
pip install git+https://github.com/jkb-novak-birne/birneD365.bc.git@main#egg=d365-business-central-lib
```

## Usage

### Initialization

To use the library, you need to initialize the `D365Wrapper` class with your credentials:

```python
from birneD365.bc import D365Wrapper

client_id = "your_client_id"
client_secret = "your_client_secret"
tenant_id = "your_tenant_id"
company_id = "your_company_id"
env_name = "your_env_name"  # e.g., "sandbox" or "production"

d365 = D365Wrapper(client_id, client_secret, tenant_id, company_id, env_name)
```

### Native API

#### Get Data

To get data from a native API endpoint with optional filtering, ordering, and pagination:

```python
filters = "Field eq 'Value'"
orderby = "Field asc"
maxpagesize = 50
native_df = d365.get_all_native_pages_as_dataframe("fixedAssets", filters, orderby, maxpagesize)
print("Native API DataFrame with Pagination:")
print(native_df)
```

### OData API

#### Get Data

To get data from an OData API endpoint with optional filtering, ordering, and pagination:

```python
filters = "Field eq 'Value'"
orderby = "Field asc"
maxpagesize = 50
odata_df = d365.get_all_odata_pages_as_dataframe("BRN_Service_Package_Line_Mileage", filters, orderby, maxpagesize)
print("OData API DataFrame with Pagination:")
print(odata_df)
```

#### Delete Data

To delete data from an OData API endpoint:

```python
endpoint = "BRN_Service_Package_Lines"
key_values = {
    "Service_Package_No": 999,
    "Service_Code": "'ADMIN FEE'"
}
status_code = d365.delete_odata(endpoint, key_values)
print("Delete OData API Status Code:")
print(status_code)
```

### Custom Native API

#### Get Data

To get data from a custom native API endpoint with optional filtering, ordering, and pagination:

```python
filters = "Field eq 'Value'"
orderby = "Field asc"
maxpagesize = 50
custom_native_df = d365.get_all_custom_native_pages_as_dataframe("contracts", filters, orderby, maxpagesize)
print("Custom Native API DataFrame with Pagination:")
print(custom_native_df)
```

## Running Tests

To run the tests, use the following command:

```bash
pytest tests/
```
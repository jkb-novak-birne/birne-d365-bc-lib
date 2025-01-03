# d365 Business Central Library

This library provides a Python interface for interacting with Microsoft Dynamics 365 Business Central using both the native API and OData protocol. It simplifies authentication and data manipulation, making it easier to integrate with Business Central.

## Features

- **Authentication Management**: Handles OAuth2 authentication using client ID and client secret.
- **Native API Interaction**: Provides methods to interact with the native API for data retrieval and manipulation.
- **OData Protocol Support**: Allows fetching and creating entities using the OData protocol.
- **Utility Functions**: Includes helper functions for token management and configuration loading.

## Installation

To install the library, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/d365-business-central-lib.git
cd d365-business-central-lib
pip install -r requirements.txt
```

## Usage

### Authentication

To authenticate and obtain an access token:

```python
from d365.auth import AuthManager

auth_manager = AuthManager()
token = auth_manager.get_access_token(client_id='your_client_id', client_secret='your_client_secret')
```

### Native API

To interact with the native API:

```python
from d365.native_api import NativeAPIClient

api_client = NativeAPIClient(token)
data = api_client.get_data('your_endpoint')
```

### OData

To work with OData entities:

```python
from d365.odata import ODataClient

odata_client = ODataClient(token)
entities = odata_client.fetch_entities('your_entity_name')
```

## Running Tests

To run the tests, use the following command:

```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
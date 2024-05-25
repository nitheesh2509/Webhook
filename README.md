# Webhook
### Project Overview

1. **Project Structure**:
   - You've created a Django project named `web_app` with an app named `core`.
   - The project follows the standard Django structure with models, views, serializers, and URLs.

2. **Django Models**:
   - **Account Model**:
     - Represents an account with fields:
       - `email`: Email address of the account (unique).
       - `account_id`: Unique UUID for each account.
       - `account_name`: Name of the account.
       - `app_secret_token`: Secret token automatically generated for the account (unique).
       - `website`: Optional field for the account's website.
     - This model is used to store information about each account.

   - **Destination Model**:
     - Represents a destination associated with an account with fields:
       - `account`: Foreign key to `Account` model, linking the destination to its account.
       - `url`: URL of the destination.
       - `http_method`: HTTP method used for the destination (e.g., GET, POST).
       - `headers`: JSON field storing headers associated with the destination.
     - This model is used to store destinations that data can be sent to from an account.

3. **Django Serializers**:
   - **AccountSerializer**:
     - Serializes and deserializes `Account` instances to and from JSON.
     - Used for creating, updating, and retrieving accounts via API endpoints.

   - **DestinationSerializer**:
     - Serializes and deserializes `Destination` instances to and from JSON.
     - Used for creating, updating, and retrieving destinations via API endpoints.

4. **API Endpoints**:
   - **Accounts API** (`/api/accounts/`):
     - Provides CRUD (Create, Read, Update, Delete) operations for accounts.
     - Includes endpoints for listing all accounts, creating a new account, retrieving details of a specific account, updating an account, and deleting an account.

   - **Destinations API** (`/api/destinations/`):
     - Provides CRUD operations for destinations.
     - Includes endpoints for listing all destinations, creating a new destination, retrieving details of a specific destination, updating a destination, and deleting a destination.
     - Additional endpoint (`/api/destinations/<account_id>/`) to retrieve all destinations associated with a specific account.

5. **Functionality**:
   - **Creating Accounts and Destinations**:
     - Accounts can be created with a unique email and optional website.
     - Upon creation, an `account_id` and `app_secret_token` are automatically generated.
     - Destinations can be associated with accounts, specifying a URL, HTTP method, and headers.

   - **Managing Data Handling and Sending**:
     - Data received through the `/server/incoming_data` endpoint includes an `app_secret_token`.
     - The app verifies the token, identifies the associated account, and sends the data to all destinations linked to that account.
     - Depending on the HTTP method of the destination, the data is sent as a query parameter or in the body.

### How It Works

1. **Setting Up Accounts and Destinations**:
   - Use the `/api/accounts/` endpoint to create accounts.
   - Use the `/api/destinations/` endpoint to create destinations and link them to accounts.

2. **Retrieving Data**:
   - Use the various API endpoints to retrieve lists of accounts and destinations.
   - Use the `/api/destinations/<account_id>/` endpoint to retrieve all destinations associated with a specific account.

3. **Sending Data**:
   - When data is sent to `/server/incoming_data`, ensure the correct `app_secret_token` is included in the request headers (`CL-X-TOKEN`).
   - The app verifies the token, identifies the account, and sends the data to all associated destinations based on the HTTP method and headers specified for each destination.

### Next Steps

- **Testing**: Test each endpoint using tools like Postman to ensure they work as expected.
- **Deployment**: Deploy your Django application to a server, such as Heroku, AWS, or DigitalOcean.
- **Documentation**: Update your documentation with detailed instructions on how to use each endpoint and the flow of data through your application.
- **Collaboration**: Share your GitHub repository with collaborators and stakeholders for feedback and collaboration.

This setup allows for flexible management of accounts and destinations, ensuring that data can be sent to multiple destinations from a single account based on specified conditions. 

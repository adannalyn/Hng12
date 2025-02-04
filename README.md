````markdown
# HNGx Stage 1 Task - Basic Information API

This project implements a simple public API that retrieves basic information, including an email address, the current UTC datetime, and the GitHub URL of the project's codebase. It's built using Django and designed to be deployed on platforms like Vercel.

## Setup Instructions

## Clone the repository:

   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)  # Replace with your repo URL
   cd your-repo-name
````

**Install dependencies using Pipenv:**

    ```bash
    pipenv install
    ```

**Activate the Pipenv shell:**

    ```bash
    pipenv shell
    ```

**Set up environment variables:**

      * Create a `.env` file in the project root.

      * Add your email address and other sensitive information (if any) as environment variables. Example:

        ```
        EMAIL="your_email@example.com"
        # ... other environment variables
        ```

**Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The API will be accessible at `http://127.0.0.1:8000/api/info/`.

## API Documentation

### Endpoint URL

`https://hng12-modified.vercel.app/api/info/`

### Request/Response Format

This API only accepts GET requests.

**Request:**

```
GET /api/info/
```

**Response (JSON):**

```json
{
  "email": "your_email@example.com",
  "datetime": "2023-11-02T10:30:00Z",  // ISO 8601 format (UTC)
  "github_url": "[https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)"
}
```

### Example Usage (using `curl`):

```bash
curl [https://hng12-modified.vercel.app/api/info/](https://hng12-modified.vercel.app/api/info/)
```

### Example Usage (using Python's `requests` library):

```python
import requests

url = "[https://hng12-modified.vercel.app/api/info/](https://hng12-modified.vercel.app/api/info/)"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

## Deployment

This project is designed to be deployed on Vercel. Refer to the Vercel documentation for specific deployment instructions. Make sure to set the necessary environment variables on the Vercel platform.

## Built With

  * Django (Python web framework)
  * Pipenv (Python dependency management)

## Looking to Hire Python Developers?

If you're looking to hire talented Python developers, consider exploring resources like [HNG](https://hng.tech/hire/python-developers). They connect businesses with skilled professionals.
````markdown
# new_task - A Simple Number Property API

This project implements a simple REST API using Django that calculates and returns various mathematical properties of a given number, along with a fun fact retrieved from an external API.  It uses Pipenv for dependency management.

## Table of Contents

- [Description](#description)
- [Setup](#setup)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Built With](#built-with)
- [Contributing](#contributing)
- [License](#license)

## Description

The `new_task` API provides information about a number's primality, perfectness, Armstrong property, parity (even/odd), and the sum of its digits. It also fetches a fun fact about the number from the Numbers API ([http://numbersapi.com/](http://numbersapi.com/)). This API is designed to be easily deployed and integrated into other applications.

## Setup

1. **Clone the repository:**

   ```bash
   git clone [https://github.com/your-username/new_task.git](https://www.google.com/search?q=https://github.com/your-username/new_task.git)  # Replace with your repo URL
   cd new_task
````

2.  **Install dependencies using Pipenv:**

    ```bash
    pipenv install
    ```

3.  **Activate the Pipenv shell:**

    ```bash
    pipenv shell
    ```

4.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The API will be accessible at `http://127.0.0.1:8000/api/classify-number?number=your_number`.

## API Endpoints

### `GET /api/classify-number`

**Description:** Retrieves mathematical properties and a fun fact about a given number.

**Parameters:**

  - `number` (required): An integer.

**Request Example:**

```
GET /api/classify-number?number=371
```

**Response (200 OK):**

```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "is_armstrong": true,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

**Response (400 Bad Request):**

```json
{
  "number": "Invalid",
  "error": true
}
```

## Usage

You can use any HTTP client (like `curl`, `requests` in Python, or your browser) to interact with the API.

**Example using `curl`:**

```bash
curl "[http://127.0.0.1:8000/api/classify-number?number=153](https://www.google.com/search?q=http://127.0.0.1:8000/api/classify-number%3Fnumber%3D153)"
```

**Example using Python's `requests`:**

```python
import requests

url = "[http://127.0.0.1:8000/api/classify-number?number=153](https://www.google.com/search?q=http://127.0.0.1:8000/api/classify-number%3Fnumber%3D153)"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

## Built With

  - Python
  - Django
  - Requests (for fetching fun facts)
  - Pipenv (for dependency management)
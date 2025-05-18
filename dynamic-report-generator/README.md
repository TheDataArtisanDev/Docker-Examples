# Dynamic Report Generator

This project demonstrates a simple Flask-based API for generating CSV reports dynamically from JSON input. The application is containerized using Docker and uses a multi-stage build for efficient image size.

## Features

- Accepts a POST request with user data in JSON format.
- Generates a CSV report and returns it as a downloadable file.
- Lightweight and easy to run in any Docker environment.

## How to Run

```bash
# Build the Docker image
docker build -t dynamic-report-generator .

# Run the container
docker run -p 5000:5000 dynamic-report-generator
```

## API Usage

### Endpoint

```
POST /generate-report
Content-Type: application/json
```

### Request Body Example

```json
{
  "users": [
    {"name": "Alice", "email": "alice@example.com", "score": 95},
    {"name": "Bob", "email": "bob@example.com", "score": 88}
  ]
}
```

### Response

- Returns a CSV file (`report.csv`) containing the user data.

## Example with curl

```bash
curl -X POST http://localhost:5000/generate-report \
  -H "Content-Type: application/json" \
  -d '{"users":[{"name":"Alice","email":"alice@example.com","score":95},{"name":"Bob","email":"bob@example.com","score":88}]}'
```

The response will be a CSV file download.

## Example with PowerShell

```powershell
Invoke-RestMethod `
  -Uri http://localhost:5000/generate-report `
  -Method POST `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{ "users": [ { "name": "Alice", "email": "alice@example.com", "score": 95 }, { "name": "Bob", "email": "bob@example.com", "score": 88 } ] }' `
  -OutFile "report1.csv"
```

This will save the CSV response as `report1.csv` in your current directory.

## Notes

- The container exposes port 5000.
- The API expects each user object to have `name`, `email`, and `score` fields.

---

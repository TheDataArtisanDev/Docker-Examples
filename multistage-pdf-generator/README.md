# Multistage PDF Generator

This project demonstrates how to use Docker multi-stage builds to create a minimal, production-ready image for a PDF generator application. Multi-stage builds help separate the build environment from the runtime environment, resulting in smaller and more secure images.

---

## What is a Multi-Stage Build?

A multi-stage build in Docker allows you to use multiple `FROM` statements in a single Dockerfile. Each stage can use a different base image and perform different tasks. Artifacts (such as installed dependencies or built files) can be copied from one stage to another, ensuring that only the necessary files are included in the final image.

---

## Example: Python PDF Generator

This repository contains a Python Flask app that generates PDFs using the `fpdf` library. The Dockerfile uses a multi-stage build to optimize the final image.

### Dockerfile Example

```dockerfile
# Stage 1 - Builder
FROM python:3.11-slim AS builder

WORKDIR /install

COPY app/requirements.txt .
RUN pip install --prefix=/install/python-packages -r requirements.txt

# Stage 2 - Runtime
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /install/python-packages /usr/local
COPY app /app

EXPOSE 5000

CMD ["python", "app.py"]
```

**How it works:**

- The first stage (`builder`) installs all dependencies into a separate directory.
- The second stage copies only the installed dependencies and application code into a fresh, minimal image.
- This results in a smaller, more secure production image.

---

## How to Run

1. **Build the Docker image:**
   ```bash
   docker build -t multistage-pdf-generator .
   ```

2. **Run the container:**
   ```bash
   docker run -p 5000:5000 multistage-pdf-generator
   ```

---

## API Usage

### Endpoint

```
POST /generate-pdf
Content-Type: application/json
```

### Request Body Example

```json
{
  "name": "Alice"
}
```

### Response

- Returns a PDF file with a greeting for the provided name.

### Example with curl

```bash
curl -X POST http://localhost:5000/generate-pdf \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice"}' --output output.pdf
```

### Example with PowerShell

```powershell
Invoke-RestMethod `
  -Uri http://localhost:5000/generate-pdf `
  -Method POST `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{ "name": "Alice" }' `
  -OutFile "output.pdf"
```

This will save the PDF response as `output.pdf` in your current directory.

---

## Benefits of Multi-Stage Builds

- **Smaller Images:** Only necessary files and dependencies are included in the final image.
- **Security:** Build tools and unnecessary packages are excluded from production.
- **Cleaner Deployments:** Only production code and assets are shipped.

---

## Best Practices

- Use minimal base images (e.g., `alpine`, `slim`).
- Copy only what is needed from the build stage.
- Clean up caches and temporary files.
- Pin dependency versions for reproducibility.
- Use `.dockerignore` to exclude unnecessary files from the build context.

---

## Troubleshooting Multi-Stage Builds

- Use `docker build --target <stage>` to debug intermediate stages.
- Use `docker image ls` and `docker history <image>` to inspect image sizes and layers.

---

## References

- [Docker Multi-Stage Builds](https://docs.docker.com/develop/develop-images/multistage-build/)
- [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Python Docker Example](https://docs.docker.com/samples/python/)

# Multistage PDF Generator

---

## Overview

This project demonstrates how to use Docker multi-stage builds to create a minimal, production-ready image for a PDF generator application. Multi-stage builds help separate the build environment from the runtime environment, resulting in smaller and more secure images.

---

## What is a Multi-Stage Build?

A multi-stage build in Docker allows you to use multiple `FROM` statements in a single Dockerfile. Each stage can use a different base image and perform different tasks. Artifacts (such as built code or generated files) can be copied from one stage to another, ensuring that only the necessary files are included in the final image.

---

## Example: Python PDF Generator

If your PDF generator is written in Python (e.g., using WeasyPrint or ReportLab):

```Dockerfile
# filepath: Dockerfile
# Stage 1: Build environment
FROM python:3.11-slim AS build
WORKDIR /src
COPY requirements.txt .
RUN pip install --user -r requirements.txt
COPY . .

# Stage 2: Runtime image
FROM python:3.11-slim
WORKDIR /app
COPY --from=build /src /app
ENV PATH="/root/.local/bin:$PATH"
CMD ["python", "pdf_generator.py"]
```

---
**How it works:**

- The first stage installs all dependencies and copies the source code.
- The second stage copies only the built app and production dependencies, resulting in a smaller image.
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
- [Node.js Docker Example](https://nodejs.org/en/docs/guides/nodejs-docker-webapp/)
- [Python Docker Example](https://docs.docker.com/samples/python/)

# Hello Docker - Simple Flask App

This is a minimal Python Flask app containerized using Docker.

## How to Run

```bash
# Build the image
docker build -t hello-docker .

# Run the container
docker run -p 5000:5000 hello-docker
```

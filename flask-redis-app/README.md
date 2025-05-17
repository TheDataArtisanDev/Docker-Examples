# Flask + Redis with Docker Compose

This project demonstrates how to containerize and orchestrate a simple multi-service application using Docker Compose. It includes a Python Flask web server that uses Redis as a backend cache to track page views. This setup introduces key concepts of service networking, dependency management, and container composition using declarative configuration.

The Flask app connects to Redis using the internal Docker network, eliminating the need for manual IP management. Docker Compose handles building the application image (defined via Dockerfile), pulling the official Redis image, and running both containers in a shared environment.

To run the application, simply execute `docker-compose up --build`, and navigate to `http://localhost:5000` in your browser. Each page refresh increments a view counter stored in Redis.

This project emphasizes:

- Defining multi-container environments using `docker-compose.yml`
- Building application images with Dockerfile
- Understanding service discovery via container hostnames
- Coordinating multiple services with simplified local development workflows

To reflect code changes, rebuild and restart the stack using `docker-compose build` and `docker-compose up`. Clean up with `docker-compose down`.

This serves as a foundational example of using Docker Compose to simulate microservices or distributed architectures in a controlled, local development environment.

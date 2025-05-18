# Docker: The Complete Guide

---

## Basic concepts

### What is Docker?

Docker is an open-source platform designed to automate the deployment, scaling, and management of applications using containerization. A container is a lightweight, standalone, executable package that includes everything needed to run a piece of software, including the code, runtime, libraries, and system tools. By using containers, Docker ensures that applications run consistently across different computing environments, from development to production.

### Virtual Machines vs Containers

Virtual Machines (VMs) and containers both provide isolated environments for running applications, but they differ fundamentally in their architecture:

- **Virtual Machines (VMs):**

  - Each VM runs a full operating system, including its own kernel, on top of a hypervisor.
  - VMs are resource-intensive, as they require significant memory and storage for each OS instance.
  - Startup times for VMs are relatively slow due to OS boot processes.
  - VMs provide strong isolation, making them suitable for running different OS types on the same hardware.
- **Containers:**

  - Containers share the host operating system’s kernel but run isolated user spaces.
  - They are lightweight, with minimal overhead, as they do not require a full OS per instance.
  - Containers start almost instantly, making them ideal for microservices and scalable applications.
  - They provide process-level isolation, which is sufficient for most application workloads.

### Docker Architecture

Docker’s architecture is composed of several key components:

- **Docker Engine:** The core part of Docker, responsible for building and running containers. It consists of:

  - **Docker Daemon (`dockerd`):** A background process that manages Docker objects such as images, containers, networks, and volumes.
  - **Docker Client (`docker`):** The command-line interface that users interact with. It sends commands to the Docker Daemon via REST API.
  - **REST API:** Enables programmatic control over Docker, allowing integration with other tools and automation scripts.
- **Images:** Docker images are immutable, read-only templates used to create containers. Images are built in layers, where each layer represents a set of file changes or instructions in the Dockerfile. Layers are cached and shared, making image builds efficient.
- **Containers:** Containers are runtime instances of Docker images. They are isolated from each other and the host, but share the host OS kernel. Containers have their own filesystem, networking, and process space.
- **Registries:** Registries are repositories for storing and distributing Docker images. The default public registry is Docker Hub, but private registries can also be used for internal image distribution.

### Docker Images

Docker images are the blueprints for containers. They are constructed from a series of layers, each corresponding to an instruction in the Dockerfile. Images are versioned and can be tagged for easy identification. Since images are immutable, any changes result in the creation of a new image layer.

- **Layered Structure:** Each image consists of multiple layers, which are stacked on top of each other. Layers are reused across images to save space and speed up builds.
- **Immutability:** Once built, images do not change. Any modification creates a new image.
- **Distribution:** Images can be pushed to and pulled from registries, enabling easy sharing and deployment.

### Docker Containers

A Docker container is a running instance of an image. Containers are isolated environments that include everything needed to run an application. They provide process and filesystem isolation, but share the host OS kernel.

- **Isolation:** Containers run in their own namespaces, providing separation from other containers and the host.
- **Ephemeral Nature:** Containers are designed to be transient. Data not stored in volumes or bind mounts is lost when the container is removed.
- **Lifecycle:** Containers can be started, stopped, paused, and deleted. They can also be restarted automatically if configured.

### Dockerfile

A Dockerfile is a text file containing a set of instructions for building a Docker image. Each instruction creates a new layer in the image. Common Dockerfile instructions include:

- `FROM`: Specifies the base image to use.
- `RUN`: Executes commands in the shell during image build.
- `COPY` and `ADD`: Copy files and directories into the image.
- `CMD` and `ENTRYPOINT`: Define the default command to run when a container starts.
- `ENV`: Sets environment variables.
- `EXPOSE`: Documents the ports the container will listen on.
- `WORKDIR`: Sets the working directory for subsequent instructions.
- `VOLUME`: Creates a mount point for external storage.

### Docker Compose

Docker Compose is a tool for defining and managing multi-container Docker applications. It uses a YAML file (`docker-compose.yml`) to configure application services, networks, and volumes.

- **Service Definition:** Each service represents a container, specifying the image, build context, environment variables, ports, and volumes.
- **Multi-Container Coordination:** Compose manages the lifecycle of all defined services, ensuring they start in the correct order and can communicate over defined networks.
- **Scaling:** Services can be scaled up or down by specifying the number of container instances.

### Volumes

Volumes are Docker’s mechanism for persisting data generated and used by containers. They allow data to exist independently of the container lifecycle.

- **Named Volumes:** Managed by Docker, stored in a specific location on the host.
- **Bind Mounts:** Map a specific file or directory on the host to the container.
- **tmpfs Mounts:** Store data in the host system’s memory only.

Volumes are essential for databases, logs, and any scenario where data persistence is required beyond the life of a container.

### Networking

Docker provides several networking options to enable communication between containers and with the outside world:

- **Bridge Network:** The default network driver. Containers on the same bridge network can communicate with each other.
- **Host Network:** Removes network isolation between the container and the Docker host, using the host’s networking directly.
- **None Network:** Disables all networking for the container.
- **Overlay Network:** Enables communication between containers running on different Docker hosts, typically used in Docker Swarm.

Custom networks can be created to provide fine-grained control over container connectivity and isolation.

### Docker Registry

A Docker registry is a storage and distribution system for Docker images.

- **Docker Hub:** The default public registry, hosting a vast collection of official and community images.
- **Private Registries:** Organizations can host their own registries for internal use, providing control over image distribution and access.
- **Image Tagging:** Images are tagged for versioning and identification (e.g., `myapp:1.0`).
- **Authentication:** Required for pushing to or pulling from private registries.

### Orchestration

Orchestration tools manage the deployment, scaling, and operation of containerized applications across clusters of machines.

- **Docker Swarm:** Docker’s native clustering and orchestration solution. It provides service discovery, load balancing, scaling, and rolling updates.
- **Kubernetes:** A widely adopted, feature-rich orchestration platform. It manages container scheduling, scaling, networking, and storage, and supports self-healing and declarative configuration.

Orchestration is essential for running containers in production at scale.

### Security Concepts

Docker incorporates several security features to isolate containers and protect the host system:

- **Namespaces:** Provide isolation for process IDs, network interfaces, mount points, users, and more.
- **Control Groups (cgroups):** Limit and prioritize resource usage (CPU, memory, disk I/O) for containers.
- **Capabilities:** Restrict the privileges available to container processes, reducing the attack surface.
- **Seccomp:** Filters system calls available to containers, preventing potentially dangerous operations.
- **User Namespaces:** Map container users to different host users, reducing the risk of privilege escalation.
- **Image Scanning:** Tools are available to scan images for known vulnerabilities.
- **Secrets Management:** Securely store and manage sensitive data such as passwords, API keys, and certificates.

### Best Practices

To ensure efficient, secure, and maintainable Docker environments, follow these best practices:

- Use minimal base images (e.g., `alpine`) to reduce image size and attack surface.
- Pin image versions to avoid unexpected changes.
- Use `.dockerignore` to exclude unnecessary files from the build context.
- Avoid storing secrets in images or environment variables.
- Regularly update images and dependencies to patch vulnerabilities.
- Run containers as non-root users whenever possible.
- Use multi-stage builds to optimize final image size.

### Troubleshooting Concepts

Effective troubleshooting in Docker involves understanding container behavior and system state:

- **Logs:** Inspect container logs to diagnose application errors or crashes.
- **Inspect:** Retrieve detailed metadata about containers, images, networks, and volumes.
- **Exec:** Run commands inside running containers for debugging or maintenance.
- **Prune:** Remove unused containers, images, networks, and volumes to free up resources and maintain a clean environment.



### Docker CLI Commands Reference

This section provides a practical explanation of commonly used Docker commands categorized by their purpose.

#### 🔧 Image Commands

* `docker build -t <image_name> .`
  * Builds an image using the Dockerfile in the current directory and tags it with a name.
* `docker build --no-cache -t <image_name> .`
  * Forces a fresh build of all layers, bypassing Docker's build cache.
* `docker images`
  * Lists all locally stored Docker images.
* `docker rmi <image_name>`
  * Removes a specified image from local storage.
* `docker image prune`
  * Deletes unused or dangling image layers to free up disk space.

#### 🏃 Container Commands

* `docker run <image>`
  * Runs a container from the specified image.
* `docker run -it <image>`
  * Runs a container in interactive mode with a terminal session.
* `docker run -d <image>`
  * Starts a container in detached mode (in the background).
* `docker run --rm <image>`
  * Runs a container and removes it automatically after it exits.
* `docker run -p 5000:5000 <image>`
  * Maps port 5000 of the host to port 5000 of the container.
* `docker run -v $(pwd)/data:/data <image>`
  * Mounts a local directory as a volume inside the container.

#### 📋 Container Lifecycle

* `docker ps`
  * Lists currently running containers.
* `docker ps -a`
  * Lists all containers, including stopped ones.
* `docker stop <container_id>`
  * Stops a running container by ID or name.
* `docker start <container_id>`
  * Starts an existing, stopped container.
* `docker restart <container_id>`
  * Restarts a running or stopped container.
* `docker rm <container_id>`
  * Deletes a container from the local system.

#### 🔍 Logs and Debugging

* `docker logs <container_id>`
  * Outputs logs from a running container.
* `docker exec -it <container_id> bash`
  * Opens an interactive shell session inside a running container.
* `docker inspect <container_id or image>`
  * Displays detailed metadata and configuration information.
* `docker stats`
  * Shows real-time metrics for container resource usage.

#### 📦 Volumes and Data

* `docker volume ls`
  * Lists all volumes managed by Docker.
* `docker volume create <name>`
  * Creates a named volume.
* `docker volume rm <name>`
  * Removes a specific volume.
* `docker volume inspect <name>`
  * Displays metadata and mount paths of a volume.

#### 🌐 Networking

* `docker network ls`
  * Lists all Docker networks.
* `docker network create <name>`
  * Creates a new custom user-defined network.
* `docker network inspect <name>`
  * Provides details about a specific network’s configuration.
* `docker network connect <network> <container>`
  * Attaches a container to a specified network.
* `docker network disconnect <network> <container>`
  * Detaches a container from a specified network.

#### 🧹 System Cleanup

* `docker system df`
  * Displays disk usage by Docker images, containers, and volumes.
* `docker system prune`
  * Removes all unused containers, networks, and dangling images.
* `docker system prune -a`
  * Aggressively cleans up all unused data including unused images.

#### 🧩 Docker Compose

* `docker-compose up`
  * Starts all services defined in `docker-compose.yml`.
* `docker-compose up --build`
  * Rebuilds images before starting services.
* `docker-compose down`
  * Stops and removes containers, networks, and volumes created by Compose.
* `docker-compose logs`
  * Displays logs for all Compose-managed services.
* `docker-compose ps`
  * Shows status and port mappings of Compose services.
* `docker-compose build`
  * Builds images defined in the Compose file without running them.

---

## References

- [Docker Official Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Docker Compose Docs](https://docs.docker.com/compose/)
- [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

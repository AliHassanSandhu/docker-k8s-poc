# Docker and Kubernetes Proof of Concept (POC)

This project demonstrates a complete containerization and deployment workflow using **Docker**, **Kubernetes**, and **FastAPI**.  
It showcases how to build, test, and deploy a lightweight Python microservice in a Kubernetes environment using modern DevOps tools and best practices.

The goal of this Proof of Concept (POC) is to create a reproducible system where a single command can build and deploy the microservice into a Kubernetes cluster with automated configurations.

---

## Features

- FastAPI-based Python microservice  
- Docker containerization with lightweight image optimization  
- Kubernetes deployment with automated health checks and scaling   
- Makefile for simplified build, test, and deployment commands  

---

## Folder Structure

```
docker-k8s-poc/
│
├── app/
│   ├── main.py
│   ├── requirements.txt
│   └── __init__.py
│
├── tests/
│   └── test_api.py
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── .github/workflows/
│   └── ci.yaml
│
├── docker-compose.yaml
├── Dockerfile
├── Makefile
└── README.md
```

---

## Prerequisites

Before setting up locally, ensure the following tools are installed:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [VS Code](https://code.visualstudio.com/download)
- [Git](https://git-scm.com/install) or [GitHub Desktop](https://desktop.github.com/download/)
- Python 3.8 or higher
- Minikube / Kind / or Docker Desktop Kubernetes (this project uses Docker Desktop Kubernetes)

---

## Local Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/AliHassanSandhu/docker-k8s-poc
cd docker-k8s-poc
```

### Step 2: Build and Run the Application

You can use either **Docker commands** or the provided **Makefile**.

#### Option 1: Using Docker directly

```bash
# Build Docker image
docker build -t docker-k8s-poc:latest .

# Run container locally
docker run -p 8000:8000 docker-k8s-poc:latest
```

Access the app at: [http://localhost:8000](http://localhost:8000)

#### Option 2: Using Makefile

```bash
make build
make run
```

---

## Kubernetes Deployment

### Step 1: Enable Kubernetes in Docker Desktop

1. Open Docker Desktop  
2. Go to **Settings → Kubernetes**  
3. Enable Kubernetes and select **Kubeadm**  
4. Wait until the cluster starts successfully

### Step 2: Deploy to Kubernetes

```bash
make k8s-deploy
```

Alternatively:

```bash
kubectl apply -f k8s/
```

Check running resources:

```bash
kubectl get pods,svc
```

Then access the app at:

```
http://localhost:<port-number>
```

---

## Running Tests

```bash
pytest
```

Expected output: all test cases should pass.

---

## Makefile Commands

| Command | Description |
|----------|-------------|
| `make build` | Build the Docker image |
| `make run` | Run the container locally |
| `make compose-up` | Run using Docker Compose |
| `make k8s-deploy` | Deploy to Kubernetes |
| `make test` | Run tests using Pytest |
| `make clean` | Clean up unused Docker resources |

---

## Versioning and Tagging

```bash
git tag v1.0.0
git push origin v1.0.0
docker build -t poc-api:v1.0.0 .
docker push <registry>/poc-api:v1.0.0
```

---

## Health Checks

**Dockerfile Example:**
```dockerfile
HEALTHCHECK CMD curl --fail http://localhost:8000/ || exit 1
```

**Kubernetes Example:**
```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8000
readinessProbe:
  httpGet:
    path: /health
    port: 8000
```

---

## Lightweight Container Optimization

- Uses **python:3.12-alpine** base image  
- Applies `--no-cache-dir` to reduce build size  
- Includes `.dockerignore` to exclude unnecessary files  
- Supports multi-stage builds for cleaner images  
---

### Documentation : [Docker-Kubernetes-Proof-of-Concept](https://drive.google.com/file/d/17vq0fs3VkPegoPoPBTToCwbV97teg6gW/view?usp=sharing)
  

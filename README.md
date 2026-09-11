# Python CI/CD Demo

A production-ready CI/CD pipeline demonstrating automated testing, containerization, and deployment.

## What This Shows

- ✅ **Flask Python Application** — Simple REST API with health checks
- ✅ **Automated Testing** — pytest tests run on every commit
- ✅ **Docker Containerization** — Multi-stage Docker builds
- ✅ **GitHub Actions CI/CD** — Automated test, build, and push pipeline
- ✅ **Docker Hub Integration** — Images automatically pushed to registry

## Tech Stack

- **Language:** Python 3.11
- **Framework:** Flask 2.3.0
- **Testing:** pytest 7.4.0
- **CI/CD:** GitHub Actions
- **Container:** Docker
- **Registry:** Docker Hub

## Quick Start

### Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Run the app
python app.py
```

The app runs on `http://localhost:5000`

### API Endpoints

- `GET /` — Returns greeting
- `GET /api/health` — Health check

### Docker

```bash
# Build image
docker build -t python-cicd-demo .

# Run container
docker run -p 5000:5000 python-cicd-demo
```

## CI/CD Pipeline

Every push triggers:
1. **Test Job** — Runs pytest
2. **Build Job** — Builds Docker image and pushes to Docker Hub

View runs: [Actions](../../actions)

## Docker Hub

Images available at: `857085/python-cicd-demo:latest`

## Files

- `app.py` — Flask application
- `test_app.py` — Test suite
- `Dockerfile` — Container configuration
- `requirements.txt` — Python dependencies
- `.github/workflows/deploy.yml` — CI/CD workflow

## What I Learned

This project demonstrates core DevOps skills:
- Container orchestration with Docker
- Automated testing and CI/CD pipelines
- GitHub Actions workflow automation
- Container registry management
- Infrastructure as Code principles

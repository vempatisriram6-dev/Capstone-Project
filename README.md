# Capstone-Project
* This project demonstrates a complete CI/CD pipeline for a 2-tier web application using modern DevOps practices.

* The system automatically builds, tests, scans, and deploys applications across multiple environments using Docker, GitHub Actions, and AWS EC2.

* The goal of this capstone is to simulate a real-world DevOps workflow from development to production with security, reliability, and automation.
---
# Project overview

This repository demonstrates how to build a CI/CD pipeline from zero, starting with source code and ending with a production deployment.

### The pipeline automatically :  ###

* Developed a 2-tier web application locally in VS Code
* Containerized frontend and backend using Docker
* pushed source code to GitHub
* Created GitHub Actions CI pipeline
* Added GitHub repository secrets
* Automated:
  * Docker
  * Unit Testing
  * Trivy security Scanning
  * Image push to Docker Hub
* Deployed the apllication to AWS EC2
* Verified deployment using healthchecks
* implemented rollback mechanism for failures
 --- 
# Application Architecture

## 2-Tier Architecture

### **Frontend** ###

* Static HTML + CSS UI
* Served using Nginx
* Lightweigt and optimized container

### **Backend** ###

* Flask REST API
* Health check endpoints
* Database connectivity
* Runs as a non-root user

### **Database** ###
* PostgreSQL (containerized)
  
### **CI/CD** ###

* GitHub Actions
* Docker Hub registry

### **Deployment** ###

* AWS EC2 using SSH
* SSH-based automated deployment
---
#  Tech Stack

| Category | Technologies |
|--------|-------------|
| Frontend | HTML, CSS, Nginx |
| Backend | Python, Flask |
| Database | PostgreSQL |
| Containers | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| Security | Trivy |
| Cloud | AWS EC2 |
| Testing | Pytest |
| Automation | Bash |
---
# CI/CD Architecture

```
Developer
   ↓
GitHub Repository
   ↓
CI Tool (Jenkins / GitHub Actions)
   ↓
Build & Test
   ↓
Docker Image Build
   ↓
Security Scan (Trivy)
   ↓
Push to Docker Hub
   ↓
Deploy to Server (EC2 / VM)

```
---
# Project Structure

```
Capstone-Project/
│
├── frontend/
│   ├── index.html
│   ├── nginx.conf
│   └── Dockerfile
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── tests/
│       └── test_app.py
│
├── scripts/
│   ├── deploy.sh
│   ├── healthcheck.sh
│   ├── rollback.sh
│
├── docker-compose.yml
├── .github/workflows/ci.yml
└── README.md

```
---
# Docker Implementation

### Backend Dockerfile
- Multi-stage build for optimized image size
- Lightweight Python base image
- Runs as a non-root user for security
- Uses environment variables for configuration

### Frontend Dockerfile
- Uses Nginx Alpine image for minimal footprint
- Serves static HTML and CSS content
- Custom Nginx configuration for routing
---
# Testing Strategy
Testing is critical part of this CI/Cd pipeline to ensure that only reliable and verified code is deployed to higher environments.

* unit tests written using pytest
* Tests executed inside Docker containers
* Automated Test Execution in CI Pipeline
* pipeline fails if tests fail
---
# Security Scanning
* Trivy Scans both frontend and backend images
* Detects HIGH and CRITICAL vulnerabilities
* Scan results displayed in pipeline logs
---
#  Environment-Specific Configuration (Staging)






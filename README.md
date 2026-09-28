# Production AWS Flask & Docker Deployment 

A production-ready DevOps implementation deploying a Dockerized Flask application leveraging Gunicorn as the WSGI server, Nginx as a reverse proxy, and AWS cloud infrastructure (EC2 + RDS MySQL).

##  Architecture Blueprint

```text
Internet ──► EC2 Security Group (Port 80) ──► Nginx (Reverse Proxy)
                                                    │
                                                    ▼
Flask App ◄─── RDS MySQL (:3306) ◄─── Gunicorn (:8000) ◄─── Docker Container
```

## Tech Stack & Components
* **Framework:** Flask (Python 3.12-slim base)
* **WSGI HTTP Server:** Gunicorn (Green Unicorn)
* **Containerization:** Docker
* **Reverse Proxy:** Nginx
* **Cloud Infrastructure:** AWS EC2 (Elastic Compute Cloud)
* **Database Platform:** AWS RDS (Relational Database Service - MySQL)

## Repository Structure
* `app.py` — Core Flask application logic with structural app and health endpoints.
* `requirements.txt` — Project app dependencies including Flask, Gunicorn, and MySQL connector.
* `Dockerfile` — Multistage/optimized container configuration for lightweight deployments.
* `.gitignore` — Strict configuration to safeguard environment parameters (`.env`) and virtual environments from tracking.

## Deployment Milestones
1. **Phase 1:** Containerize and validate Flask/Gunicorn runtime environments locally.
2. **Phase 2:** Launch and network security profiles across AWS EC2 and RDS instances.
3. **Phase 3:** Orchestrate an isolated Docker environment inside EC2 communicating with RDS.
4. **Phase 4:** Layer Nginx front-facing configurations to safely proxy incoming web traffic.

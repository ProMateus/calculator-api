# Calculator API

## Opis projektu

Calculator API to aplikacja napisana w Pythonie z wykorzystaniem frameworka FastAPI. Umożliwia wykonywanie podstawowych działań matematycznych poprzez REST API.

Obsługiwane operacje:
- dodawanie
- odejmowanie
- mnożenie
- dzielenie

Aplikacja została skonteneryzowana przy użyciu Dockera i wdrożona w Amazon Web Services z wykorzystaniem Amazon ECS oraz Amazon ECR. Proces budowania i wdrażania został zautomatyzowany przy pomocy GitHub Actions.

---

# Architektura

```
GitHub
   │
   ▼
GitHub Actions
   │
   ▼
Docker Build
   │
   ▼
Amazon ECR
   │
   ▼
Amazon ECS (Fargate)
   │
   ▼
Public URL
```

---

# Technologie

- Python 3.11
- FastAPI
- Uvicorn
- Docker
- GitHub Actions
- Amazon ECR
- Amazon ECS Fargate
- Terraform
- Pytest

---

# Uruchomienie lokalne

Utworzenie środowiska:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instalacja zależności:

```bash
pip install -r requirements.txt
```

Uruchomienie aplikacji:

```bash
uvicorn app.main:app --reload
```

Aplikacja będzie dostępna pod adresem:

```
http://127.0.0.1:8000/docs
```

---

# Budowanie obrazu Docker

```bash
docker build -t calculator-api .
```

Uruchomienie kontenera:

```bash
docker run -p 8000:8000 calculator-api
```

---

# CI/CD

Pipeline GitHub Actions wykonuje:

- instalację zależności,
- uruchomienie testów,
- budowę obrazu Docker,
- wysłanie obrazu do Amazon ECR,
- wdrożenie nowej wersji aplikacji do Amazon ECS.

---

# Infrastruktura

Kod infrastruktury został przygotowany przy użyciu Terraform.

Projekt wykorzystuje:

- Amazon ECR
- Amazon ECS Fargate
- IAM
- VPC
- Security Groups

---

# Endpointy

- GET /
- GET /health
- GET /version
- POST /calculate

---

# Publiczny adres aplikacji

Swagger UI:

```
http://34.209.124.6:8000/docs
```

OpenAPI:

```
http://34.209.124.6:8000/openapi.json
```

---

# Repozytorium GitHub

https://github.com/ProMateus/calculator-api
---

# Autor

Mateusz Krzywdziński

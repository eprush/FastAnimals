# FastAnimals
This is a web service that returns a random photo of a cat, dog, or fox upon request, having previously processed it.

## Technology stack
- Python >=3.13
- FastAPI
- SQLAlchemy
- PostgreSQL
- Celery
- Redis
- Docker
- Alembic
- Pillow
- pdm
- RESTAPI

## Application Launch Guide
First of all you should сlone this repository ``` git clone https://github.com/eprush/FastAnimals ```. 
And after that create a file .env using the following example

```
ENVIRONMENT: str = "production"
POSTGRES_HOST: str = "localhost"
POSTGRES_PORT: str = "5432"
POSTGRES_DB: str = "fast_animals"
POSTGRES_USERNAME: str = "postgres"
POSTGRES_PASSWORD: str = "example"
POSTGRES_TEST_DB: str = "test_db"
POOL_SIZE: int = 20
CAT_API_KEY: str = "peace_35mbejkg4uuVzdso0012"
EMAIL_ADDRESS: str = "your_email@domain.com"
EMAIL_PASSWORD: str = "your_password"
CELERY_BROKER_URL: str = "redis://redis:1234/5"
CELERY_RESULT_BACKEND: str = "redis://redis:1234/5"
```

There are two ways to launch a project:
### From terminal
1. Install all dependencies ``` pip install pdm ``` and ``` pdm install ```
2. Do needed migrations ``` alembic upgrade head ```
3. Run the app locally on your device ``` uvicorn app.main:app --host 0.0.0.0 --port 8080 ```

### From Docker
1. Launch the app on a container ``` docker compose up --build ```


## User's Guide

### API link
You need to follow by http://localhost:8080/docs

### Available Queries
1. /animal/cat — request for a cat image.
2. /animal/dog — request for a dog image.
3. /animal/fox — request for a fox image.
4. /history — request to get the query history.
5. /history/static/<uuid> — request to get a certain image by its unique identifier (UUID).

### Project structure
- 📁 app - source code directory.
    - 📁 core - configuration directory.
    - 📁 endpoints - endpoints and routers directory.
    - 📁 integrations - integrations with external API directory.
    - 📁 migrations - migration versions directory.
    - 📁 models - ORM models directory.
    - 📁 repositories - repo directory.
    - 📁 schemas - schemas directory.
    - 📁 services - internal services directory.
    - 📁 static - images directory.
    - 📁 tasks - background tasks directory.
    - 📄 main.py - launching script
- 📄 LICENCE - licence file.
- 📄 .env - environment file.
- 📄 .gitignore - git settings file.
- 📄 Dockerfile - file for docker image creation.
- 📄 docker-compose.yaml - file for launch project correctly.
- 📄 pyproject.toml - dependency description file.
- 📄 alembic.ini - migration configuration file.
- 📄 README.md - guides file.

# FastAnimals
A test task is a small web service that returns a random photo of a cat, dog, or fox upon request, having previously processed it.

## Technology stack
- Python >=3.13
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pillow
- RESTAPI
- Docker

## Application Launch Guide
1. Clone this repository ``` git clone https://github.com/eprush/FastAnimals ```
2. Install all dependencies ``` pip install -r requirements.txt ```
3. Run the app locally on your device ``` fastapi dev app/main.py ```

## User's Guide
To get an image, you need to send a request via the appropriate link. In response, the service will provide the processed image.

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
    - 📁 models - ORM models directory.
    - 📁 repositories - repo directory.
    - 📁 schemas - schemas directory.
    - 📁 services - internal services directory.
    - 📁 static - images directory.
    - 📄 main.py - launching script
- 📄 LICENCE - licence file.
- 📄 .env - environment file.
- 📄 .gitignore - git settings file.
- 📄 Dockerfile - file for docker image creation.
- 📄 requirements.txt - dependecies file.
- 📄 README.md - guides file.

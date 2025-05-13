# FastAnimals
A test task is a small web service that returns a random photo of a cat, dog, or fox upon request, having previously processed it.

## Application Launch Guide
1. Clone this repository ``` git clone https://github.com/eprush/FastAnimals ```
2. Install all dependencies ``` pip install -r requirements.txt ```
3. Run the app locally on your device ``` fastapi dev app/main.py ```

## User's Guide
### Available Queries
1. /animal/cat — request for a cat image.
2. /animal/dog — request for a dog image.
3. /animal/fox — request for a fox image.
4. /history — request to get the query history.
5. /history/static/<uuid> — request to get a certain image by its unique identifier (UUID).

To get an image, you need to send a request via the appropriate link. In response, the service will provide the processed image.
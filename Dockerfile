# our base image
FROM python:3.13

# specify the port number the container should expose
EXPOSE 8000

# run the application
CMD ["fastapi", "dev", "app/main.py"]
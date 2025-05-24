# our base image
FROM python:3.13

# change the working directory
WORKDIR /app

COPY ./app/main.py /app
COPY ./requirements.txt /app

# install dependencies inside the image
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# specify the port number the container should expose
#EXPOSE 8000

# run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
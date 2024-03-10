# Uses the official Python 3.9 slim image with the Buster base (lightweight)
FROM python:3.9-slim-buster

# Set the working directory inside the container to /app
WORKDIR /app

# Copies all files from the current directory (.) into the working directory
COPY . /app

# Installs Python dependencies listed in requirements.txt
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg libsm6 libxext6 libgl1-mesa-glx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt

# Exposes port $PORT for container communication (for local deployment)
# EXPOSE 3000

# Run the Python script app.py with Gunicorn as the WSGI server (for Heroku deployment).
# CMD ["python3", "/app/app.py"]

# Exposes port $PORT for container communication (for Heroku deployment)
EXPOSE $PORT

# Run the Python script app.py with Gunicorn as the WSGI server (for Heroku deployment).
CMD gunicorn --workers=1 --bind 0.0.0.0:$PORT app:app
# Dockerfile

# Use a Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /Assignment-3

# Copy the current directory contents into the container at /Assignment-3
COPY . /Assignment-3

# Install Flask in the container using a different mirror
RUN pip install -i https://pypi.python.org/simple --default-timeout=100 flask

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]

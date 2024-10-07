# Use a Python base image (this gives us Python pre-installed)
FROM python:3.9-slim

# Set the working directory in the Docker container to /app
WORKDIR /app

# Copy your project files into the Docker container
COPY . .

# Install the Python libraries specified in your requirements.txt
RUN pip install -r requirements.txt

# Command to run your Python script when the container starts
# replace main.py with the code you want to run
CMD ["python", "main.py"]

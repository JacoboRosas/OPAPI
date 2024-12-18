# Use the official Python image from the Docker Hub
FROM python:3.12.3-slim

# Install PostgreSQL development packages
RUN apt-get update && apt-get install -y libpq-dev gcc && apt-get clean

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . /app

# Tambien funciona COPY . .
# Expose the port your app runs on
EXPOSE 8000

# Start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
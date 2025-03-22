# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port Django will run on
EXPOSE 8001

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]

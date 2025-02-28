# Use the official Python 3.10: image as a base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install python-dotenv
RUN pip install python-dotenv

# Copy the rest of the application code into the container
COPY . .

# Expose port 6379 for Redis communication (default Redis port)
EXPOSE 6379

# Set the default command to run your Python app
CMD ["python", "app/feeder.py"]


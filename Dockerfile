# Start from Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy your code into container
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app files
COPY app.py .

# Run the app
CMD ["python", "app.py"]
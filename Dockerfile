# Use a lightweight Python image
FROM python:3.11

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY app_flask.py .

# Expose the Flask port
EXPOSE 5000

# Command to run the app
CMD ["python", "app_flask.py"]

FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy project files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Set environment variables
ENV FLASK_ENV=production
ENV GUNICORN_CMD_ARGS="--workers=3 --bind=0.0.0.0:8887"

# Expose the port the app runs on
EXPOSE 8887

# Start the app with Gunicorn
CMD ["gunicorn", "main:app"]


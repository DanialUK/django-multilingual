FROM python:3.10-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apk add --no-cache \
    build-base \
    libpq \
    python3-dev \
    libjpeg-turbo-dev \
    zlib-dev \
    gettext \
    redis \
    curl

# Install Python dependencies
COPY requirements.txt requirements-celery.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements-celery.txt

# Create media and static directories
RUN mkdir -p /app/media /app/static

# Copy project
COPY . .

# Create necessary directories for Celery
RUN mkdir -p /var/log/celery /var/run/celery

# Set permissions
RUN chown -R nobody:nobody /var/log/celery /var/run/celery

# Compile message files
RUN python manage.py compilemessages

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 
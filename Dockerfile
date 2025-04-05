FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    gettext \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create media and static directories
RUN mkdir -p /app/media /app/static

# Copy project
COPY . .

# Compile message files
RUN python manage.py compilemessages

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 
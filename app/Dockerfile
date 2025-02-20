# Base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define build-time arguments for user and group
ARG APP_DIR=/app



# Install necessary build and runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \ 
    curl \
    gnupg \
    gcc \
    python3-dev \
    musl-dev \
    libpq-dev \
    gettext \
    # Makefile
    make \
    # For VectorStore 
    cmake \
    build-essential \ 
    libopenblas-dev \
    libomp-dev \
    libblas-dev \
    && rm -rf /var/lib/apt/lists/*



# Set up the application directory
WORKDIR ${APP_DIR}

# Copy the application code to the /app directory
COPY . ${APP_DIR} 

# Ensure executable permissions for the scripts
# Don't forget to remove volumes from the docker-compose file
RUN chmod +x ${APP_DIR}/start_app.sh 


# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip --no-cache-dir

# Install Python packages
RUN pip install -r requirements.txt --no-cache-dir



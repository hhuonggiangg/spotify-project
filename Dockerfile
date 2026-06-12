FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Create Streamlit config directory and config file
RUN mkdir -p ~/.streamlit && \
    echo "[server]\n\
headless = true\n\
port = 8501\n\
enableXsrfProtection = false\n\
enableCORS = false\n\
\n\
[client]\n\
showErrorDetails = false\n\
showMenuItems = false\n\
\n\
[logger]\n\
level = error" > ~/.streamlit/config.toml

# Run Streamlit
CMD ["streamlit", "run", "app.py", \
     "--server.port=8501", \
     "--server.address=0.0.0.0", \
     "--server.headless=true", \
     "--logger.level=error"]

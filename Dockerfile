FROM ubuntu:22.04

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3.11 \
    python3-pip \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install ollama
RUN curl -L https://ollama.ai/install.sh | sh

# Copy requirements and install Python dependencies
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

# Copy application files
COPY . /app/

# Expose ports for both Streamlit and Ollama
EXPOSE 8501
EXPOSE 11434

# Create a startup script
RUN echo '#!/bin/bash\n\
    ollama serve & \n\
    sleep 5 && \
    ollama pull llama3.1 && \
    ollama pull llama3.2 && \
    streamlit run app.py --server.port=8501 --server.address=0.0.0.0\n\
    ' > /app/start.sh && chmod +x /app/start.sh

# Set the startup script as the entrypoint
ENTRYPOINT ["/app/start.sh"]
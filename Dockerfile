# 1. Base image (Debian-based → apt works)
FROM python:3.13-slim

# 2. Install system dependencies (SWI-Prolog)
RUN apt-get update && \
    apt-get install -y swi-prolog && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# 3. Set working directory inside container
WORKDIR /careeradvisor

# 4. Copy dependency file
COPY requirements.txt .

# 5. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy project files
COPY . .

# 7. Expose Streamlit port
EXPOSE 8501

# 8. Run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]


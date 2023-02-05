FROM python:3.9.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Copy project
COPY  download_market_data.py /app

# Instantiate database
ENTRYPOINT [ "python3", "/app/download_market_data.py" ]

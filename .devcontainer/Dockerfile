FROM senzing/senzingapi-tools:staging

#
# Development
#
RUN apt-get update && apt-get install -y \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

RUN pip install poetry


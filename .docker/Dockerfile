FROM python:3.13.4-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
ENV NPM_CONFIG_CACHE=/tmp/.npm

# Install system packages as root, including sudo
RUN apt-get update\
    && apt-get install -y --no-install-recommends \
        bash \
        build-essential \
        libpq-dev \
        gettext \
        curl \
        nodejs \
        npm \
        sudo \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*
    
RUN pip install --upgrade pip

WORKDIR /Blog-Website-Thing

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy scripts
COPY ./.docker/dev-start /
COPY ./.docker/prod-start /
COPY ./.docker/test-start /

RUN chmod +x /dev-start /prod-start /test-start

COPY . .
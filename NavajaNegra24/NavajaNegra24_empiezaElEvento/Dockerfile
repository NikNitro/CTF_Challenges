FROM python:3.11-alpine

# Install packages
RUN apk add --update --no-cache libcurl curl-dev build-base supervisor


# Upgrade pip
RUN python -m pip install --upgrade pip

# Install dependencies
RUN pip install Flask requests

# Setup app
RUN mkdir -p /app

# Switch working environment
WORKDIR /app

# Add application
COPY challenge .

# Setup supervisor
COPY config/supervisord.conf /etc/supervisord.conf

# Expose port the server is reachable on
EXPOSE 8998

# Disable pycache
ENV PYTHONDONTWRITEBYTECODE=1

# Run supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]

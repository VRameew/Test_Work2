# Pull base image
FROM python:3

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /Example

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=150KI9eJUqnk32EDJHBxsNrvmyniw6jQ7' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\n/p')&id=150KI9eJUqnk32EDJHBxsNrvmyniw6jQ7" -O ffmpeg.exe && rm -rf /tmp/cookies.txt

# Copy project
COPY . .
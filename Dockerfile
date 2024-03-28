FROM python:3.12.2-alpine3.19

ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN apk add
RUN apk add --update docker openrc
RUN rc-update add docker boot
RUN apk add --no-cache bash

# Required to install mysqlclient with Pip
RUN apk add --no-cache python3
RUN apk add --no-cache --virtual .build-deps py-pip python3-dev musl-dev gcc mariadb-dev
RUN pip install mysql

# Install pipenv
RUN pip install --upgrade pip 
RUN pip install pipenv

# Install application dependencies
COPY Pipfile Pipfile.lock /app/
# We use the --system flag so packages are installed into the system python
# and not into a virtualenv. Docker containers don't need virtual environments. 
RUN pipenv install --system

# Copy the application files into the image
COPY . /app/


CMD ["pipenv", "run", "python", "my/app.py", "0.0.0.0:8000"]
# Expose port 8000 on the container
EXPOSE 8000
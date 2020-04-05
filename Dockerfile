# FROM python:3.8
# ENV PYTHONUNBUFFERED 1

# # Allows docker to cache installed dependencies between builds
# COPY ./requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# # Adds our application code to the image
# COPY . code
# WORKDIR code

# EXPOSE 8000

# # Run the production server
# CMD newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - covidFYI.wsgi:application

# FROM python:3-alpine
FROM tejasa97/alpine_python
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache postgresql-libs bash && \
	apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev
	# apk add postgresql-dev gcc python3-dev musl-dev

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir
RUN apk --purge del .build-deps

# Adds our application code to the image
COPY . code
WORKDIR code

EXPOSE 8000

# Run the production server
CMD newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - covidFYI.wsgi:application
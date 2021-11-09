#
# Build Docker image:
# $ docker build --tag timezones:v0.0.1 .
#
# Run Docker container (from image build above)
# $ docker run -p 8000:8000 timezones:v0.0.1
#

FROM python:3.9-alpine

WORKDIR /app

# install system dependencies
RUN apk update && apk add python3-dev gcc libc-dev geos

# install project requirements
COPY requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt

COPY timezones/ .
COPY docker-entrypoint.sh docker-entrypoint.sh

EXPOSE 8000

RUN ls -alh /app/

ENTRYPOINT ["sh", "/app/docker-entrypoint.sh"]

CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi:app"]
FROM python:3.8-alpine

LABEL maintainer="minnigaliev-r@yandex.ru"

RUN mkdir -p /app/{config,src}
COPY requirements/requirements.txt /app/config/

WORKDIR /app/src

RUN \
    apk add libpq && \
    apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
    pip install -r /app/config/requirements.txt && \
    apk --purge del .build-deps

COPY config/entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/bin/sh", "/entrypoint.sh"]

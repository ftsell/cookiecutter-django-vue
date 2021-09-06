FROM docker.io/node:16-alpine as node-build
WORKDIR /app
COPY src/{{ cookiecutter.project_slug }}_frontend/{{ cookiecutter.project_slug }}_vue/ /app/
RUN yarn install --pure-lockfile
RUN yarn run build

FROM docker.io/tiangolo/uvicorn-gunicorn:python3.8-slim

# add system dependencies
RUN pip3 install pipenv
WORKDIR /app

# install dependencies
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --system --ignore-pipfile

# add remaining sources
COPY src /app/
COPY .docker/prestart.sh /app/
RUN ln -sf /app/{{ cookiecutter.project_slug }}/asgi.py /app/main.py
COPY --from=node-build /app/dist /app/{{ cookiecutter.project_slug }}_frontend/{{ cookiecutter.project_slug }}_vue/dist/

# setup recommended container config
RUN mkdir /app/data
ENV DJANGO_CONFIGURATION=Prod
ENV BL_DB_PATH=/app/data/db.sqlite

# add additional metadata
VOLUME /app/data
LABEL org.opencontainers.image.title="{{ cookiecutter.project_name }}"


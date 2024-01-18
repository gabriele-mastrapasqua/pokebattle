# step 1 - builder image
FROM python:3.8 as builder

WORKDIR /app

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# Install project dependencies
COPY pyproject.toml poetry.lock /app/

RUN pip install poetry && poetry install --no-root --no-dev && rm -rf $POETRY_CACHE_DIR


# step 2 - runtime image
FROM python:3.8-slim-buster as runtime

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}


# Copy the project files into the container
WORKDIR /app
COPY pokebattle pokebattle

ENTRYPOINT ["python", "-m", "pokebattle.main"]
#RUN ["python", "-m", "pokebattle.main"]

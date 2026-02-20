FROM python:3.14-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /src

# Install dependencies
RUN --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen

COPY . .

# Place executables in the environment at the front of the path
ENV PATH="/src/.venv/bin:$PATH"

# APP ENTRYPOINT

# RUN chmod a+x /src/docker/entry_point.sh
# ENTRYPOINT ["python", "run.py"]
# Reset the entrypoint, don't invoke `uv`
ENTRYPOINT ["python", "main.py"]

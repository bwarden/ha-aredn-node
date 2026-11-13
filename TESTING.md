# Testing

## Prerequisites

- Docker
- The repository checked out locally

## Development container

Create and start a container from the devcontainer definition:

```sh
docker run -d --name ha-aredn-dev \
  -p 8123:8123 \
  -v "$PWD":/workspaces/hacs-aredn-node \
  -w /workspaces/hacs-aredn-node \
  mcr.microsoft.com/devcontainers/python:3.14 sleep infinity
```

Install dependencies inside the container:

```sh
docker exec ha-aredn-dev bash -lc "cd /workspaces/hacs-aredn-node && scripts/setup"
docker exec ha-aredn-dev bash -lc "pip install pytest pytest-asyncio pytest-aiohttp"
```

## Running tests

```sh
docker exec ha-aredn-dev bash -lc \
  "cd /workspaces/hacs-aredn-node && PYTHONPATH=/workspaces/hacs-aredn-node/custom_components python -m pytest -q"
```

## Linting

```sh
docker exec ha-aredn-dev bash -lc "cd /workspaces/hacs-aredn-node && scripts/lint"
```

## Home Assistant instance

Start a local Home Assistant instance with the integration loaded:

```sh
docker exec ha-aredn-dev bash -lc "cd /workspaces/hacs-aredn-node && scripts/develop"
```
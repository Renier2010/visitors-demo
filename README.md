# visitors-demo

A small Flask visit counter that stores its count in Redis. Docker Compose runs both services together.

I wrote the Dockerfile and docker-compose.yml myself as a rebuild exercise after week 1 of my DevOps learning plan, with feedback on my mistakes from Claude (an AI assistant made by Anthropic).

## What it shows
- Dockerfile with layer caching and a non-root user
- Docker Compose with two services (app and Redis)
- A named volume so the count survives restarts
- Redis is not published to the host, only the app is (port 8080)

## Run it

    docker compose up -d --build
    curl localhost:8080
    curl localhost:8080/health

The count keeps going after `docker compose down` and `docker compose up -d`, because it lives in the `redisdata` volume.

## Clean up

    docker compose down

Use `docker compose down -v` to also delete the stored count.

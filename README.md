# GitHub Gists API

## Run locally (Docker)

docker build -t github-gists-api .
docker run -p 8080:8080 github-gists-api

## API Endpoint

GET /{username}

Example:
http://localhost:8080/octocat

## Features

- Fetch public gists
- Pagination support
- Error handling
- Automated tests
- Dockerized

## Run Tests

pytest
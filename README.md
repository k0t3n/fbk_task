# FBK task

Aiohttp-based application used for saving incoming requests to PostgreSQL. 

## Requirements

* [Python 3.7](https://www.python.org/downloads/release/python-370/)
* [aiohttp 3.6.2](https://github.com/aio-libs/aiohttp/releases/tag/v3.6.2)

Full list of all requirements available in requirements.txt

## Configuration
Copy `.env-example` and configure variables.
```shell script
cp .env-example .env
```

## Usage
Start containers using `docker-compose`.
```shell script
docker-compose up
```

Request example:
```shell script
curl --location --request POST 'http://127.0.0.1:8080' \
--header 'Content-Type: text/plain' \
--data-raw 'test'
```

## What could I do but did not
 * K8s config
 * Cover with tests
 * Configure CI/CD

## License
MIT

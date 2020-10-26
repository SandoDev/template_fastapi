# Template FastAPI

## Table of Contents

- [Template FastAPI](#template-fastapi)
  - [Table of Contents](#table-of-contents)
  - [About The Project](#about-the-project)
    - [Built With](#built-with)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Instalation (Local)](#instalation-local)
    - [Execution (Local)](#execution-local)
    - [Instalation (Docker)](#instalation-docker)
    - [Execution (Docker)](#execution-docker)
  - [Documentation of project](#documentation-of-project)
    - [Folder structure](#folder-structure)
    - [Architecture](#architecture)
    - [Workflows](#workflows)


## About The Project
This project is a template for build microservices in framework fastapi.
This documentation is focused on the developer who wants to execute and contribute to the project.

### Built With
* Language: [Python3](https://www.python.org/)
* Framework: [FastAPI](https://fastapi.tiangolo.com/)
* Database: [MongoDB](https://www.mongodb.com/)
* Container: [Docker](https://www.docker.com/) 


## Getting Started
The prerequisites and installation is explained as follows:

### Prerequisites
It is necessary to have it installed on the machine where the project will be mounted:
- **Python3** language
- Python **pip** package manager
- Virtual environment **virtualenv** (or other virtual environment)
- **Mongo** database engine
- **Docker** container manager (for installation with docker)

### Instalation (Local)

### Execution (Local)
```sh
gunicorn --env FASTAPI_SETTINGS_MODULE=config.settings config.api:app --bind=0.0.0.0:8001 --timeout=300 -k=uvicorn.workers.UvicornWorker --reload
```

### Instalation (Docker)

### Execution (Docker)

## Documentation of project
### Folder structure
### Architecture
### Workflows

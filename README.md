# Medium_API_Clone

Medium API Clone. This was made using Django, the Django Rest Framework, Docker Compose, Celery, Flower, Redis, NGINX, Elasticsearch, Pytest, Mailhog, and PostgreSQL

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This API is not currently deployed.

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

## Table of Contents

1. [Technologies_Used](#technologies_used)
2. [Features](#features)
3. [Usage](#usage)
4. [Testing](#testing)

## Technologies_Used

- **API:**

  - Django
  - Django Rest Framework

- **Database:**

  - PostgreSQL

- **Reverse Proxy / Load Balancer **

  - NGINX

  **Asynchronous task processing**

  - Celery (with Flower as a GUI)
  - Redis (Message Broker to manage queuing and distribution of tasks)

  **Multi-Container Application**

  - docker Compose

  **Test Email Functionality (in development)**

  - Mailhog

## Features

This API uses JWT access tokens with refresh cookies to handle user authentication and authorization. Elasticsearch has been added to provide article search functionality. The app is set up using Docker Compose and is currently made up of eight containers. Celery has been added to asynchronously handle background tasks, to make the application run faster and more smoothly. Redis has been employed as a celery message broker. The application uses a PostgreSQL database. Shell scripts have been employed throughout the application to start certain processes and make sure things run smoothly.

In development a Makefile was created to make is easy to quickly execute those long docker compose commands. Pytest was used to create unit tests and generate a coverage report. I only did one hundred percent test coverage for the User app of the project.

Flake8, isort, and black were used as linters to make the code all nice and pretty and increase readability.

Even though it may have been overkill. Virtual environments were set up within Python containers.

Swagger was used to document the API.

This project currently has no front end. But, by interacting with the backend users can create an account, login, create articles, change or reset their password (via email - mailhog test smtp server), bookmark articles (create and remove), and search articles. Once a user creates an account, django signals is used to automatically create a user profile. Users can follow or unfollow other users, update their profiles, add ratings to articles, and provide responses to articles. There is also a clap feature (which medium uses) which is a like feature.

## Installation

### Prerequesites

- [Docker](https://www.docker.com/)

This application, in its current state, is made up of three docker images. One for the Django API, one for the postgres database, and one for the uwsgi reverse proxy. All you need is Docker and docker compose to run the application.

- [Make](https://lists.gnu.org/archive/html/info-gnu/2020-01/msg00004.html)

A make file was created and can be viewed for a list of aliased commands. This makes managing docker containers, linting, testing, and testing report generation very easy.

### Setup

1. Clone the repository:

```
git clone https://github.com/Jkhall81/Medium_API_Clone.git
```

2. Navigate to the project root directory:

```
cd Medium_API_Clone
```

3. Create a '.envs' folder, inside make a '.local' folder, with the following two files:

.django

CELERY_BROKER=redis://redis:6379/0

DOMAIN=localhost:8080
EMAIL_PORT=1025
CELERY_FLOWER_USER=
CELERY_FLOWER_PASSWORD=
SIGNING_KEY=

.postgres

POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
DATABASE_URL=postgres://your-user:your-password@Postgres:5432/your-db

create usernames, passwords, and fill in other fields as you wish.

4. Build and run the Docker containers:

```
make build
```

5. Interact with the API at localhost:8080/swagger/ or use Postman and use the urls provided in the documentation page provided.

create an account, and start adding data.

## Usage

For API documentation, go to localhost:8080/swagger/ after the server is running.

## Testing

All testing done with Django, the Django Rest Framework test client, and Pytest. Tests are located within test folders of the User app.

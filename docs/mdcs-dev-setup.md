# Set up a Development Environment for the CDCS

The setup was done on MacOS. 

## Clone a CDCS project

Create a workspace folder for CDCS development. 

```shell
mkdir workspace 
cd workspace
```

Find a CDCS project on GitHub and clone it. For example, for the MDCS:

```shell
git clone https://github.com/usnistgov/MDCS.git
git checkout master
```

## Python environment

Download and install [Pyenv](https://github.com/pyenv/pyenv#installation) and 
[Pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv#installation) to configure 
a python environment with all the required python packages. 

### Create a new environment

Install a version of Python supported by the CDCS (see `python_requires` in [setup.py](https://github.com/usnistgov/core_main_app/blob/master/setup.py)):

```shell
pyenv install 3.8
```

```shell
pyenv virtualenv 3.8 core
pyenv virtualenvs
```

### Install required python packages

Activate the environment and install the required python packages.

```
pyenv activate core
cd mdcs
pip install -r requirements.txt
pip install -r requirements.core.txt
pip install core_main_app[develop]
```

**Notes**:
- `requirements.txt` contains all third-party python dependencies,
- `requirements.core.txt` contains all CDCS core dependencies,
- `core_main_app[develop]` contains additional packages used for development.

## Setup the CDCS stack

Before starting the CDCS web server, a few components need to be started and configured:
- Redis,
- PostgreSQL (optional),
- MongoDB (optional).

To do so, you can either:
- download and start the stack natively (see [installation instructions](https://github.com/usnistgov/MDCS/blob/master/docs/mdcs-2.0-install-pypi.md#1-install-supporting-applications-on-your-host-system))
- start services using docker containers (see below).
  
### Deploy the stack via containers

Below is an example of a `docker-compose.yml` file to deploy PostgreSQL, MongoDB and Redis for development.
You can copy these files, fill in values in the `.env` file and start the stack.  More information 
about running the CDCS with docker can be found in the [CDCS-Docker](https://github.com/usnistgov/cdcs-docker)
repository.

**File hierarchy:**
```shell
| mongo
  | mongo-init.sh
| .env
| docker-compose.yml
```

**docker-compose.yml**
```yaml
version: "3"
services:
  curator_postgres:
    image: postgres:${POSTGRES_VERSION}
    container_name: dev_postgres
    restart: always
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    ports:
      - 5432:5432
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASS}
      - POSTGRES_DB=${POSTGRES_DB}
  curator_mongo:
    image: mongo:${MONGO_VERSION}
    container_name: dev_mongo
    restart: always
    environment:
      - MONGO_INITDB_ROOT_USERNAME=${MONGO_ADMIN_USER}
      - MONGO_INITDB_ROOT_PASSWORD=${MONGO_ADMIN_PASS}
      - MONGO_INITDB_DATABASE=${MONGO_DB}
      - MONGO_USER=${MONGO_USER}
      - MONGO_PASS=${MONGO_PASS}
    ports:
      - 27017:27017
    volumes:
      - mongo_data:/data/db/
      - ./mongo/mongo-init.sh:/docker-entrypoint-initdb.d/mongo-init.sh:ro
    command: "--auth --noscripting"
  curator_redis:
    image: redis:${REDIS_VERSION}
    container_name: dev_redis
    restart: always
    ports:
      - 6379:6379
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  mongo_data:
  redis_data:
```

**mongo/mongo-init.sh**
```shell
echo "Creating curator user..."
echo '
    use '${MONGO_INITDB_DATABASE}'
    db.createUser(
        {
            user: "'${MONGO_USER}'",
            pwd: "'${MONGO_PASS}'",
            roles: [ "readWrite" ]
        }
    )
    exit' | mongosh
```

**.env**
```shell
# TODO: Set values for the databases configuration and credentials
POSTGRES_USER=
POSTGRES_PASS=
POSTGRES_DB=
MONGO_ADMIN_USER=
MONGO_ADMIN_PASS=
MONGO_USER=
MONGO_PASS=
MONGO_DB=
REDIS_PASS=

# TODO: Set versions for the components of the CDCS stack
MONGO_VERSION=6.0
REDIS_VERSION=7.0
POSTGRES_VERSION=14
```

**Start the stack:**
```shell
docker-compose up -d
```

**Stop the stack:**
```shell
docker-compose down
```

**Stop the stack and remove ALL data:**
```shell
docker-compose down -v
```

## Connect CDCS server to the stack

Copy the `.env.dev.example` file from the mdcs folder and rename it `.env`. This file should not be pushed to the git repository.
Then fill the values in `.env` file. Make sure to use the same credentials used to initialize the dev components from the previous section.
This `.env` file also has a few extra settings that are specific to the Django/CDCS server, make sure to provide a value for these.

```shell
# TODO: Set values for the databases configuration and credentials 
#  (Set the same values used in .env for docker-compose.yml file)
POSTGRES_USER=
POSTGRES_PASS=
POSTGRES_DB=
MONGO_ADMIN_USER=
MONGO_ADMIN_PASS=
MONGO_USER=
MONGO_PASS=
MONGO_DB=
REDIS_PASS=

# TODO: Set Django/CDCS settings
DJANGO_SECRET_KEY=
SERVER_URI=
SERVER_NAME=
```

See [installation_instructions](https://github.com/usnistgov/MDCS/blob/master/docs/mdcs-2.0-install-pypi.md#edit-and-save-install_pathmdcs-mastermdcssettingspy-file)
for more information about CDCS settings.

## PyCharm

Download and install [PyCharm](https://www.jetbrains.com/pycharm/download/).

### Open the CDCS workspace

Open project: Select workspace folder

### Select Python Interpreter

PyCharm > Preferences > Project Interpreter

Select /path/to/env/core/bin/python

### Add run configurations

#### Migrate

Script:                 mdcs/manage.py

Script parameters:      migrate

Environment variables:  DJANGO_SETTINGS_MODULE=mdcs.dev_settings

Run migrate to initialize the database (and then again anytime a change is made to models/permissions).

#### Create a Super User

Script:                 mdcs/manage.py

Script parameters:      createsuperuser

Environment variables:  DJANGO_SETTINGS_MODULE=mdcs.dev_settings

Emulate terminal in output console

Run createsuperuser to create the first user of the system (and then anytime the database is deleted).

#### Start Celery worker (optional)

Script:                 /path/to/env/core/bin/celery

Script parameters:      -A mdcs worker -E -l debug -P solo

Environment variables:  DJANGO_SETTINGS_MODULE=mdcs.dev_settings

Run celery and have it running in background (can be run in debug mode).


#### Run Server

Script:                 mdcs/manage.py

Script parameters:      runserver

Environment variables:  DJANGO_SETTINGS_MODULE=mdcs.dev_settings

Run runserver to deploy the webserver (can be run in debug mode).

#### Add an application (optional)

To modify a core application or create a new application for the CDCS, you can either clone
an existing app in the workspace folder or create a new folder and start the development.

In the case of an existing core app, you can let PyCharm know to use the one from the workspace 
instead of the one from the env with: 

Right Click on app folder: Mark Directory as > Sources Root. 

The folder icon should turn blue.
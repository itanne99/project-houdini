# project-houdini
This software stack was generated with [Compose Generator](https://www.compose-generator.com). <br>
The following sections contain instructions about the selected services and instructions for setting them up.

## FastAPI
FastAPI is a high-performance, easy to learn, fast to code and ready for production framework for building APIs. It is based on Python 3.6+ and can handle massive amounts of requests in parallel due to its asynchronous programming style.

### Setup
FastAPI is considered as backend service and can therefore be found in backends collection, when generating the compose configuration with Compose Generator.

### Usage
Compose Generator provides a basic Hello World API out of the box which can be found at the url root.

## PostgreSQL Database
PostgreSQL or for short 'Postgres' is a relational database management system.

### Setup
Compose Generator will ask you for the name of a dedicated database and the name of a dedicated user for your application. This database and user will be created on the first startup of the database container. Furthermore the cli automatically generates database user password for you, so you don't need to specify them yourself.


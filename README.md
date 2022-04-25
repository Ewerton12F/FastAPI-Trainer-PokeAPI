# FastAPI-Trainer-PokeAPI _(in progress)_
The same [Trainer-PokeAPI](https://github.com/Ewerton12F/Trainer-PokeAPI) project, but made with FastAPI.

# Tutorial

1️⃣ - Make sure you have installed Python and Docker 👇

* Download [Python](https://www.python.org/downloads/)
* Donwload [Docker](https://docs.docker.com/desktop/windows/install/)

2️⃣ - Download files [here](https://github.com/Ewerton12F/FastAPI-Trainer-PokeAPI/archive/refs/heads/master.zip) or clone the project 👇

```sh
$ git clone git@github.com:Ewerton12F/FastAPI-Trainer-PokeAPI.git
```

3️⃣ - Once inside the main directory you can create a virtual enviroment and activate it 👇

```sh
$ virtualenv venv
$ source venv/bin/activate
```

4️⃣ - Install packages 👇

```sh
$ pip install fastapi uvicorn starlette pymongo pydantic
```

5️⃣ - Build the Docker Image 👇

```sh
$ docker build -t myimage .
```

6️⃣ - Start the Docker Container 👇

```sh
$ docker run -d --name mycontainer -p 80:80 myimage
```

7️⃣ - Access docs

http://127.0.0.1/docs

# Directory Tree

```
├── app
│   ├── config
│   |   └── database.py
│   ├── models
│   |   ├── pokemon_model.py
│   |   └── trainer_model.py
│   ├── routes
│   |   └── api_route.py
│   ├── schemas
│   |   ├── pokemon_schema.py
│   |   └── trainer_schema.py
│   ├── __init__.py
│   └── main.py
├── venv
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── README.md
└── requirements.txt
```

# Dependencies

## FastAPI

* **OpenAPI for API creation**, including declarations of path operations, parameters, body requests etc.

* Automatic data model documentation with **JSON Schema** (as OpenApi itself is based on JSON Schema).

* **Automatic docs**: Interactive API documentation (**OpenAPI**).

* **No new syntax to learn**. Just standard modern **Python**.

## Uvicorn

* **ASGI SERVER**

## starlette

🚧

## Pymongo

🚧

## pydantic

🚧

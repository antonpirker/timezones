# timezones

Small microservice that returns the name of the timezone for a location specified by lat/lon


# Development

* Create virtual env
  ```bash
  cd timezones
  python3 -m venv .venv
  source .venv/bin/activate
  ```

* Install requirements
  ```bash
  pip install -r requirements.txt
  ```

* Install pre commit hooks
  ```bash
  pre-commit install
  ``` 

* Start development server
  ```bash
  FLASK_APP=timezones flask run
  ```

* Point you browser to http://localhost:5000


# Running tests

Make sure you have the virtual environment set up and the requirements installed (see "Development" above)

* Change into project directory
  ```bash
  cd timezones
  ```

* Run tests
  ```bash
  pytest
  ```


# Building Docker image

```bash
docker build --tag timezones:v0.0.1 .
```

# Running Docker container

```bash
docker run -p 8000:8000 timezones:v0.0.1
```

Point you browser to: http://localhost:8000

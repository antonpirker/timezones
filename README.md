# timezones

Small microservice that gives one the name of timezone for a position specified by lat/lon


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
  ```
  pre-commit install
  ``` 

* Start development server
  ```bash
  FLASK_APP=timezones flask run
  ```

* Point you browser to http://localhost:5000

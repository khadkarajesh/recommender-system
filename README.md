# Recommender System

Provide recommendation in ecommerce application

## Used Technologies

* Flask
* Python
* Streamlit
* Postgresql

## Steps to Run Application

1. [Install Dependencies](#install-dependencies)
2. [Run API](#run-api)
3. [Run Frontend](#run-frontend)

### Install Dependencies

1. Create a virtual environment with python3
   ```shell
   python3 -m virtualenv venv
   ```
2. Activate the virtual environment:
   ```shell
   cd venv
   source /bin/activate
   ```
2. Install dependencies
   ```shell
   pip install -r requirements.txt
   ```

### Run API

1. Configure the database Create database and add .env file in ```api/.env```. template of ```.env``` is as follows:
   ```shell
   DATABASE_NAME =
   DATABASE_PORT =
   USER_NAME =
   USER_PASSWORD =
   ```
2. Navigate to root of the project
3. Set environment variables
   ```bash
   export FLASK_APP=app:create_app
   export APP_SETTINGS="api.config.DevelopmentConfig"
   ```
4. Run Flask
   ```bash
   flask run
   ```

### Run Frontend

1. Navigate to the ```/frontend``` directory of application
2. Run streamlit application as:

```bash
   streamlit run run.py
```



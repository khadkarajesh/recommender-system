# Recommender System

It is ecommerce based recommendation engine built on operational data one of the ecommerce application. It uses the hybrid approach to recommend products. Hybrid approach combines both attribute of user, items to solve the problem of cold start and data sparsity. User attributes: Age, Gender and Items attributes: Price, Brand, Category has been considered along with interaction's purchase, click, wishlist to built model

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

1. Run streamlit application as:

```bash
   streamlit run streamlit_app.py
```



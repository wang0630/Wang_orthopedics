# 汪骨外科診所
A websit built with Flask, jinja2, mongodb and docker.

## Front-end page:
1. Use Scss for the front-end styling.
2. Use jinja2 template for generate cleaner and maintainable html code.
3. Use axios for http request.
4. Use flask-wtform for use login.

## Back-end route:
1. Use flask_assets to generate minified css and js from src code automatically.
2. Use flask-login for auth router.

## Local launching:
### Old way
1. ```python3 -m venv env ``` to create the virtual venv
2. ```source env/bin/activate ``` activate the virtual venv
3. ```pip3 install -r requirements.txt ``` to install all dependcenies
4. ```python3 run.py ``` to run the server
### New way
1. Should create ```mongodata``` folder first for mongodb to connect
2. Simply ```docker-compose -f docker-compose.dev.yml up -d --force-recreate```


todo:
1. show kicked out message to user if not logged in
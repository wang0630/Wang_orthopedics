# 汪骨外科診所
This website is totally responsive both on big srceen device and small screen ones.(see the mixin for example!)

## Front-end page:
1. Use Scss for the front-end styling.
2. Use jinja2 template for generate cleaner and maintainable html code.
3. Use axios for http request.
4. Use flask-wtform for use login.

## Back-end route:
1. Use flask as the framework instead of Node.js for simplicity.
2. Includes basic routes and use flask_assets to generate minified css and js from src code automatically.
3. Use flask-login for auth router.

## Local launching:
1. ```python3 -m venv env ``` to create the virtual venv
2. ```source env/bin/activate ``` activate the virtual venv
3. ```pip3 install -r requirements.txt ``` to install all dependcenies
4. ```python3 run.py ``` to run the server

## Testing:
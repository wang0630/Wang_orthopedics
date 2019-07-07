# 汪骨外科診所

## Front-end page:
1. Use Scss for the front-end styling.
2. This website is totally responsive both on big srceen device or small screen ones.(see the mixin for example!)
3. Use jinja2 template for generate cleaner and maintainable html code.

## Back-end route:
1. I select to use flask and python3 as the framework instead of Node.js for simplicity.
2. Includes basic routes and use flask_assets to generate css code from Scss automatically.

## Local testing:
1. ```python3 -m venv env ``` to create the virtual venv
2. ```source env/bin/activate ``` activate the virtual venv
3. ```pip3 install -r requirements.txt ``` to install all dependcenies
4. ```python3 run.py ``` to run the server
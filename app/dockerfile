FROM python:3.7

ARG rootPath=/wang-orthopedics

RUN mkdir -p ${rootPath}

WORKDIR ${rootPath}

COPY requirements.txt .

RUN python3 -m venv env \
  && . env/bin/activate \
  && pip3 install -r requirements.txt

COPY . .

CMD . env/bin/activate && python3 run.py

EXPOSE 5000

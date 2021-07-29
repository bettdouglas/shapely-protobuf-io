FROM python:3.8-slim
RUN python -m pip install --upgrade pip

COPY requirements.txt /opt/app/requirements.txt

WORKDIR /opt/app

# RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r requirements.txt
RUN pip install -r requirements.txt

COPY . /opt/app/

CMD [ "python", "server.py" ]

# gcloud beta run deploy countries --source .
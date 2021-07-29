# FROM python:3.8-slim
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY . /app
ENV APP_HOME /app

WORKDIR $APP_HOME
COPY . ./

RUN pip install -r requirements.txt

# CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 app.main:app
# RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r requirements.txt

# RUN pip install fastapi uvicorn

# EXPOSE 80

# COPY ./app /app

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", :$PORT]
CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 main:app
# gcloud builds submit --tag gcr.io/bitnami-oyzgng8y5a/countries_fastapi
# gcloud run deploy --image gcr.io/bitnami-oyzgng8y5a/countries_fastapi --platform managed

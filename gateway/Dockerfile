FROM python:3.11
WORKDIR /user/src
COPY ./requirements.txt /user/src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /user/src/requirements.txt
COPY ./app /user/src/app
WORKDIR /user/src/app

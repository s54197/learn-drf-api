FROM python:3.9-alpine

# recommended for python
ENV PYTHONUNBUFFERED 1    

# copy local requirement to docker file
COPY ./requirements.txt /requirements.txt

# install dependencies in docker req. file
RUN pip install -r /requirements.txt

# create a dir named app in docker and access the dir
RUN mkdir /app
WORKDIR /app

# copy local app to docker app
COPY ./app /app

# -D user only able to run the docker without other privilege (for security of not using root)
RUN adduser -D user
USER user


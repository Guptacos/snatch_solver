FROM python:3

RUN apt-get update && apt-get install -y python3-pip python-virtualenv libcairo2-dev libgirepository1.0-dev

# Create a virtualenv for the application dependencies.
RUN virtualenv -p python3 /env
ENV PATH /env/bin:$PATH

ADD requirements.txt /app/requirements.txt
RUN /env/bin/pip install --upgrade pip && /env/bin/pip install -r /app/requirements.txt
ADD . /app

#CMD gunicorn -b :$PORT mysite.wsgi
CMD python /app/manage.py runserver --verbosity 3 0:8000 
# [END docker]

FROM python:latest

WORKDIR /PollProject
COPY requirements.txt /PollProject
COPY PollProject /PollProject


RUN apt-get -y update && apt-get -y upgrade && \
pip install -r requirements.txt && cd PollProject 

CMD ["python3", "manage.py", "migrate"]
CMD ["python3", "manage.py", "runserver","0.0.0.0:8000"]


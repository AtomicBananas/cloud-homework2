FROM python:3-alpine

RUN mkdir -p /home/data
RUN mkdir -p /home/output

WORKDIR /usr/src/app

COPY homework2.py ./homework2.py

CMD ["python", "./homework2.py"]

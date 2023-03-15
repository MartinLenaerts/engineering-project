FROM ubuntu
RUN apt-get update && \
    apt-get install -y python3 python3-pip graphviz
WORKDIR /home/app

COPY . .

RUN python3 -m pip install pydot mypy
RUN mypy **/*.py
ENTRYPOINT ["python3", "main.py"]
FROM python:3.10

WORKDIR /app

COPY install.py .

COPY images/. .

RUN apt-get update

RUN apt-get -y install texlive-latex-base

RUN pip install -i https://test.pypi.org/simple/ latex-fluentpy

RUN python3 install.py

RUN pdflatex example.tex
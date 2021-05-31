FROM python:3.8
LABEL maintainer "Meinhard Ploner <dummy@host.com>"
WORKDIR /code
COPY requirements.txt /
RUN pip install mysql-connector-python
RUN pip install pandas
RUN pip install dash
RUN pip install psycopg2-binary
RUN pip install -r /requirements.txt
COPY ./Graficas ./
EXPOSE 8050
CMD ["python", "./Graficas/Grafica.py"]

FROM python:3.11
COPY requirements.txt app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

EXPOSE 8502

ENTRYPOINT ["streamlit","run"]

CMD ["app.py"]
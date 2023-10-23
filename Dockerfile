FROM python:3.9.16

WORKDIR /app

EXPOSE 5000

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

CMD ["python", "app.py"]
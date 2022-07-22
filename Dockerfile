FROM python:3.8-slim

USER 1000

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["launch.py"]
ENTRYPOINT ["python","-u"]
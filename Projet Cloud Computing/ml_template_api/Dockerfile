FROM python:3.6-slim

WORKDIR /app

COPY . .

#Execution d'une commande dans le conteneur
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip3 \
    vim \
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python","./main.py"]
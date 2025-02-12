FROM debian:bookworm-slim

EXPOSE 5000

RUN apt update && \
    apt install -y python3-flask python3-waitress

WORKDIR /app

ADD server.py server.py
ADD helper helper

CMD ["python3", "server.py"]

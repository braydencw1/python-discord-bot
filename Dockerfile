From python:3.11
RUN useradd -u 1000 -m -s /bin/bash user
RUN apt update -y && apt upgrade -y
USER user
RUN pip3 install pip --upgrade
RUN pip3 install discord.py python-dotenv requests paramiko psycopg2-binary
WORKDIR /morthyc

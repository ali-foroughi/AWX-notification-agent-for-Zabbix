FROM ubuntu:22.04
COPY zabbix-release_latest_6.0+ubuntu22.04_all.deb .
RUN dpkg -i zabbix-release_latest_6.0+ubuntu22.04_all.deb
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    zabbix-sender \
&& apt-get autoremove -y && apt-get autoclean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app
RUN pip install --r requirements.txt
CMD ["python3", "main.py"]


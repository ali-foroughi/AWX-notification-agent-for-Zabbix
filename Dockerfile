FROM reg.zcore.local/proxy_cache/ubuntu:22.04
RUN sed -i 's/archive.ubuntu.com/ubuntu.zcore.local/g' /etc/apt/sources.list && \
    sed -i 's/security.ubuntu.com/ubuntu.zcore.local/g' /etc/apt/sources.list
COPY zabbix-release_latest_6.0+ubuntu22.04_all.deb .
RUN dpkg -i zabbix-release_latest_6.0+ubuntu22.04_all.deb
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    zabbix-sender \
&& apt-get autoremove -y && apt-get autoclean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app
RUN pip  install --index-url http://172.20.14.54:5000/index/ --trusted-host 172.20.14.54 -r requirements.txt
CMD ["python3", "main.py"]


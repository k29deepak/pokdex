FROM faucet/python3

WORKDIR /opt

COPY requirements.txt .
COPY run-app.sh .

RUN pip install -r requirements.txt && chmod 777 run-app.sh

ENTRYPOINT [ "/bin/bash", "-l", "-c" ]

CMD ["/opt/run-app.sh"]

FROM teamvaders/vincenzobot:latest

RUN git clone https://github.com/XRAJVEER09OP/Plugins.git /root/vincenzobot

WORKDIR /root/vincenzobot

RUN pip3 install -U -r requirements.txt

ENV PATH="/home/vincenzobot/bin:$PATH"

CMD ["python3", "-m", "vincenzobot"]

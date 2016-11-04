FROM alpine:3.4

COPY Python3Tester.py /root/Python3Tester.py
COPY Python3TesterTest.py /root/Python3TesterTest.py

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache && \
    cd /root && \
    echo "python3 /root/Python3Tester.py \"\$@\"" > run.sh && \
    chmod 755 run.sh 
    
ENTRYPOINT ["/bin/sh", "/root/run.sh"]
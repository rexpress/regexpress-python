FROM regexpress/base:latest

COPY Python3Tester.py /root/Python3Tester.py
COPY Python3TesterTest.py /root/Python3TesterTest.py

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache && \
    cd /root && \
    echo "arg=();for var in \"\$@\";do arg+=(\"\$(echo -n \"\$var\" | base64 -d)\"); done; python3 /root/Python3Tester.py \"\${arg[@]}\"" > run.sh && \
    chmod 755 run.sh 
    
ENTRYPOINT ["/bin/bash", "/root/run.sh"]
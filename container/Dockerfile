ARG JAVA_V=11-jre-slim
ARG PY_V=python3.7
ARG SPARK_V=spark-3.1.1

FROM openjdk:${JAVA_V}

RUN apt-get update -y && apt-get install -y libzbar-dev bash gcc git libc-dev curl wget vim nano \
    && apt-get install -y iputils-ping telnet openssh-client net-tools \
    man unzip vim-tiny bc openssh-server thrift-compiler netcat sudo \
    && apt-get install -y build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean


RUN set -ex && \
    sed -i 's/http:\/\/deb.\(.*\)/https:\/\/deb.\1/g' /etc/apt/sources.list && \
    apt-get update && \
    ln -s /lib /lib64 && \
    apt-get install -y bash tini libc6 libpam-modules libnss3 procps && \
    rm /bin/sh && \
    ln -sv /bin/bash /bin/sh && \
    echo "auth required pam_wheel.so use_uid" >> /etc/pam.d/su && \
    chgrp root /etc/passwd && chmod ug+rw /etc/passwd && \
    rm -rf /var/cache/apt/*

#install python3.7
RUN apt-get update && apt-get install -y software-properties-common && \
    apt-add-repository -r ppa:armagetronad-dev/ppa && \
    apt-get update && apt-get install -y ${PY_V} python3-pip \
    python3-distutils python3-setuptools && \
    ${PY_V} -m pip install pip --upgrade pip && \
    echo "alias python=${PY_V}" >> ~/.bashrc && \
    export PATH=${PATH}:/usr/bin/${PY_V} && \
    /bin/bash -c "source ~/.bashrc" && \
    update-alternatives --install /usr/bin/python python /usr/bin/${PY_V} 1 && \
    update-alternatives --set python /usr/bin/${PY_V}

# install spark
RUN wget --no-verbose https://downloads.apache.org/spark/${SPARK_V}/${SPARK_V}-bin-hadoop3.2.tgz && \
    tar -xzvf ${SPARK_V}-bin-hadoop3.2.tgz && \
    mv ${SPARK_V}-bin-hadoop3.2 /opt/spark && \
    rm -rf ${SPARK_V}-bin-hadoop3.2.tgz

ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin
ENV PATH=$PATH:$SPARK_HOME/sbin
ENV PYTHONPATH=$SPARK_HOME/python3:$SPARK_HOME/python3/lib/py4j-0.10.7-src.zip:$PYTHONPATH

COPY container/requirements.txt requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf requirements.txt

RUN mkdir -p /opt/work-dir
COPY container/pi.py /opt/work-dir

COPY container/entrypoint.sh /opt/
COPY container/decom.sh /opt/

RUN chmod g+w /opt/work-dir
RUN chmod a+x /opt/decom.sh
RUN chmod a+x /opt/entrypoint.sh

WORKDIR /opt/work-dir
ENTRYPOINT [ "/opt/entrypoint.sh" ]
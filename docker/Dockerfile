FROM ubuntu:disco

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    build-essential=12.6ubuntu1 \
    git=1:2.20.1-2ubuntu1 \
    gnupg=2.2.12-1ubuntu3 \
    python3-dev=3.7.3-1 \
    python3-pip=18.1-5 \
    python3-setuptools=40.8.0-1 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/local/bin/python
RUN ln -s /usr/bin/pip3 /usr/local/bin/pip

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
RUN echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" >> /etc/apt/sources.list.d/mongodb-org-4.0.list

ENV TZ=Etc/UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    mongodb-org=4.0.10 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
	&& rm -rf /var/lib/mongodb \
	&& mv /etc/mongod.conf /etc/mongod.conf.orig

RUN pip install wheel==0.33.4

#hadolint ignore=DL3013
RUN pip install cloudmesh-installer 

RUN mkdir -p /cloudmesh
WORKDIR /cloudmesh

RUN cloudmesh-installer git clone storage
RUN cloudmesh-installer install storage -e

COPY cloudmesh/cloudmesh4.yaml /root/.cloudmesh/cloudmesh4.yaml
RUN cms admin mongo create

COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod 755 /usr/local/bin/docker-entrypoint.sh
RUN ln -s usr/local/bin/docker-entrypoint.sh / # backwards compat
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["bash"]

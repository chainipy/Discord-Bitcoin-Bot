FROM debian:stable
MAINTAINER Tim Tedford (montara@gmail.com)

RUN apt-get update && \
    apt-get -qqy install --no-install-recommends \
        autoconf \
        automake \
        build-essential \
        ca-certificates \
        git \
        mercurial \
        cmake \
        libass-dev \
        libgpac-dev \
        libtheora-dev \
        libtool \
        libvdpau-dev \
        libvorbis-dev \
        pkg-config \
        texi2html \
        zlib1g-dev \
        libmp3lame-dev \
        wget \
	python3 \
        python3-pip \
	libopus0 \
        yasm && \
    apt-get -qqy clean && \
    rm -rf /var/lib/apt/lists/*

ADD Bitcoin-Bot.py /
ADD bot_config.py /
#RUN apt-get update && apt-get -y install ffmpeg libopus0
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN python3 -m pip install discord.py
RUN python3 -m pip install requests

CMD [ "python", "./Bitcoin-Bot.py" ]

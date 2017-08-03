FROM python:3
ADD Bitcoin-Bot.py /
ADD bot_config.py /
RUN apt-get -y install ffmpeg
RUN apt-get -y install libopus0
RUN pip install discord.py
RUN pip install requests

CMD [ "python", "./Bitcoin-Bot.py" ]

FROM python:3
ADD Bitcoin-Bot.py /
ADD bot_config.py /
RUN pip install discord.py
RUN pip install requests

CMD [ "python", "./BitCoin-Bot.py" ]

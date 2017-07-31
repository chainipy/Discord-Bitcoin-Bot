from discord.ext import commands
import requests
from bot_config import BOT_USER_TOKEN

description = '''Bitcoin [BTC] price bot.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def btc():
    """fetches bitcoin price."""
    url = 'https://blockchain.info/ticker'
    resp = requests.get(url)
    btcprice = resp.json()['USD']
    # btc = resp.json()[currency]
    await bot.say('Last:\t**' + btcprice['symbol'] + str(btcprice['last'])
                  + '**\nBuy:\t**' + btcprice['symbol'] + str(btcprice['buy'])
                  + '**\nSell:\t**' + btcprice['symbol'] + str(btcprice['sell']) + '**')

@bot.command()
async def price(currency : str):
    """fetches bitcoin price."""
    currency = currency.upper()
    url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + currency + '&tsyms=BTC,USD'
    resp = requests.get(url)
    rdata = resp.json()
    if "Response" in rdata:
        if rdata["Response"] == "Error":
            return
    #display = rdata["DISPLAY"]

    btcprice = rdata["DISPLAY"][currency]['BTC']
    usdprice = rdata["DISPLAY"][currency]['USD']

    await bot.say("Current price for **" + currency + "**\n"
                  + 'Last:\t\t**' + str(btcprice['PRICE']) + " (" + str(usdprice['PRICE']) + ")**\n"
                  + 'Volume (24h):\t**' + str(btcprice['VOLUME24HOURTO']) + " (" + str(usdprice['VOLUME24HOURTO']) + ")**\n"
                  + 'Change (24h):\t**' + str(btcprice['CHANGE24HOUR']) + '**')

bot.run(BOT_USER_TOKEN)


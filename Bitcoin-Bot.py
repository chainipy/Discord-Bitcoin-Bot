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
async def hardfork():
    import datetime

    delta = datetime.datetime(2017, 8, 1, 12, 20) - datetime.datetime.now()
    seconds = (delta).total_seconds()
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    timestamp = "**%d** Hours **%02d** Minutes **%02d** Seconds" % (h, m, s)
    await bot.say("Time until hardfork: " + timestamp)

@bot.command()
async def marketcap():
    url = 'https://api.coinmarketcap.com/v1/global/'
    resp = requests.get(url)
    rdata = resp.json()

    market_cap = rdata["total_market_cap_usd"]
    market_vol = rdata["total_24h_volume_usd"]
    bitcoin_percent = rdata["bitcoin_percentage_of_market_cap"]
    # active_currencies = rdata["active_currencies"]
    # active_assets = rdata["active_assets"]
    # active_markets = rdata["active_markets"]

    await bot.say("Current market cap **$" + "{:,}".format(market_cap) + "**\n"
                  + 'Volume (24h):\t\t**$' + "{:,}".format(market_vol) + "**\n"
                  + 'Bitcoin % of Market:\t**' + str(bitcoin_percent) + "%**\n")


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
    if currency == 'BTC':
        url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + currency + '&tsyms=USD'
        resp = requests.get(url)
        rdata = resp.json()
        if "Response" in rdata:
            if rdata["Response"] == "Error":
                return
        #display = rdata["DISPLAY"]

        usdprice = rdata["DISPLAY"][currency]['USD']

        await bot.say("Current price for **" + currency + "**\n"
                      + 'Last:\t\t**' + str(usdprice['PRICE']) + "**\n"
                      + 'Volume (24h):\t**' + str(usdprice['VOLUME24HOURTO']) + "**\n"
                      + 'Change (24h):\t**' + str(usdprice['CHANGE24HOUR']) + " (" + str(usdprice['CHANGEPCT24HOUR']) + '%)**')
        return
    else:
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
                      + 'Volume (24h):\t**' + str(btcprice['VOLUME24HOURTO']) + "**\n"
                      + 'Change (24h):\t**' + str(btcprice['CHANGE24HOUR']) + " (" + str(btcprice['CHANGEPCT24HOUR']) + '%)**')

bot.run(BOT_USER_TOKEN)


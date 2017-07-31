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
async def btc(currency : str):
    """fetches bitcoin price."""
    url = 'https://blockchain.info/ticker'
    resp = requests.get(url)
    btc = resp.json()[currency]
    await bot.say(btc['symbol'] + ' ' + str(btc['last']))

bot.run(BOT_USER_TOKEN)

import discord
import pathlib
from discord.ext import commands
from configparser import ConfigParser
from customExceptions import NoMentions



currentPath = pathlib.Path(__file__).parent.absolute()
privateConfig = ConfigParser()
privateConfig.read(currentPath / "private/config.ini")
config = ConfigParser()
config.read(currentPath / "config.ini")

bot = commands.Bot(command_prefix=config["BotConfig"]["prefix"])

##########
# Events #
##########
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Scouting this server... ?help"))

@bot.event
async def on_command_error(ctx, error):
    print(f"Context: {ctx.command} | Error: {error}") # debug only



############
# Commands #
############
@bot.command()
async def ping(ctx):
    await ctx.send(f"Ping: {round(bot.latency * 1000)} ms")

@bot.command()
async def lock(ctx, time:int=None, typeTime: str=None):
    channel = ctx.channel
    mentions = (ctx.message.mentions + ctx.message.role_mentions)
    if len(mentions) == 0:
        raise NoMentions


if __name__ == "__main__":
    bot.run(privateConfig["Keys"]["development"])
import os
import discord
import logging
from dotenv import load_dotenv

from convert_data import convert_to_geocord
from get_data import get_5day_weather, get_48h_weather, get_7day_weather, get_current_weather

load_dotenv()
client = discord.Client()

OPENWEATHER_API = os.getenv("OPENWEATHER_API")
GEOCODING_API = os.getenv("GEOCODING_API")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

error_msg = ["Wrong message format, see ?weatherbot help for help", "Wrong command format", "Location unavaiable, check for spelling errors"]
help = "?weatherbot commands: \n?weatherbot - greets user \n?weatherbot -help - displays help message \n" \
       "----------------------------------------------------\n" \
       "commands to request weather data \n?weather [location] [specification]\nwhere specification is: \n" \
       "current - displays current data \n" \
       "5days - displays weather for 5 days in 3h steps \n" \
       "48h - displays weather for 48h in hour steps \n" \
       "7days - displays daily weather for 7 days"

##logging, default is disabled, use for debugging purposes
log = False
if log:
    logging.basicConfig(filename = "debug.log", filemode = "w", format = "%(levelname)s - %(message)s")
else:
    logging.basicConfig(filename="debug.log", filemode="w", format="%(levelname)s - %(message)s", level = logging.CRITICAL) ##no critical messages will be shown

def request_data(location, specification):
    location = convert_to_geocord(location, GEOCODING_API)

    if specification == "current":
        return get_current_weather(location, OPENWEATHER_API)
    elif specification == "5days":
        return get_5day_weather(location, OPENWEATHER_API)
    elif specification == "48h":
        return get_48h_weather(location, OPENWEATHER_API)
    elif specification == "7days":
        return get_7day_weather(location, OPENWEATHER_API)

    logging.error(error_msg[1])
    return error_msg[1]

@client.event
async def on_message(message):
    if message.author.bot or message.author == client.user:
        return

    if message.content.startswith("?weatherbot"):
        content = message.content.split(" ")
        logging.info("Initialized")
        if len(content) > 2:
            logging.error(error_msg[0])
            await message.channel.send(error_msg[0])
            return
        if len(content) == 1:
            await message.channel.send("Ready to serve")
            return
        elif len(content) == 2:
            if content[1] != "help":
                logging.error(error_msg[0])
                await message.channel.send(error_msg[0])
                return
            else:
                await message.channel.send(help)
                return

    if message.content.startswith("?weather"):
        content = message.content.split()
        logging.info("Accepting commands")
        if len(content) != 3:
            logging.error(error_msg[1])
            await message.channel.send(error_msg[1])
            return
        else:
            location = content[1]
            logging.info(f"Requesting data for {location}")
            specification = content[2]
            title = f"Weather for location {location} for {specification} is : \n"
            output = request_data(location, specification)
            embed = discord.Embed(title = title, description = output)
            await message.channel.send(embed = embed)
            return

client.run(DISCORD_TOKEN)






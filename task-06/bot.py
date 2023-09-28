import discord
import requests
import csv
from bs4 import BeautifulSoup
import datetime
from datetime import datetime

import scrapper

month = datetime.now().month
year = datetime.now().year
date = datetime.now().day



def run_discord_bot():
    TOKEN = "MTE1MDYzMjA5NDg4NDcwNDI5Nw.GeW_On.BEHhTlv_phv-PrLZ23g8K7uC3NB_0BuHk4OK5Q"
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
    
    @client.event
    async def on_message(msg):
        if msg.author == client.user:
            return
        username=str(msg.author)
        usr_msg=str(msg.content)
        channel = str(msg.channel)

        print(f"{username} said: {usr_msg} ({channel})")

        if usr_msg == "!livescore":
            opp,text1=scrapper.scrape()
            await msg.channel.send("fetching livescores...")
            await msg.channel.send(opp[0])
            await msg.channel.send(opp[1])
            '''
            if "won by" in text1:
                pass
            else:
                await msg.channel.send(opp[1])
                '''
            await msg.channel.send(text1)
            await msg.channel.send(str(date)+"/"+str(month)+"/"+str(year))

        elif usr_msg == "!csv":
            await msg.channel.send("getting file..")
            await msg.channel.send(file=discord.File('scores.csv'))
        elif usr_msg == "!help":
            await msg.channel.send("!livescore - for scores")
            await msg.channel.send("!csv - for score data.csv")
        else:
            pass

    client.run(TOKEN)
    
if __name__=="__main__":
    run_discord_bot()

import discord
import requests
import csv
from bs4 import BeautifulSoup
import datetime
from datetime import datetime

month = datetime.now().month
year = datetime.now().year
date = datetime.now().day

url = "https://www.espncricinfo.com/live-cricket-score"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

live_match = soup.find(class_='ds-flex ds-flex-col ds-mt-2 ds-mb-2')
text=live_match.text

try:
    text1=soup.find(class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo').text
except Exception:
    text1=""

text2=soup.findAll(class_='ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1')


opp = []
x=0
for i in text2:
    x+=1
    opp.append(i.text)
    if x==2:break



with open("scores.csv","a+") as f:
    wobj=csv.writer(f,delimiter=",")
    wobj.writerow([opp[0],opp[1],text1,str(date)+"/"+str(month)+"/"+str(year)])


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
            await msg.channel.send("fetching livescores...")
            await msg.channel.send(opp[0])
            await msg.channel.send(opp[1])
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

import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime
month = datetime.now().month
year = datetime.now().year
date = datetime.now().day

    
url = "https://www.espncricinfo.com/live-cricket-score"
def scrape():
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
    return opp,text1


import urllib3
from bs4 import BeautifulSoup
import urllib
import re
import pandas as pd
class Starters:
    def __init__(self):
        url = 'https://www.futbolfantasy.com/'
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, features="lxml")
        teams = soup('a',class_ ='team')
        Teams = []
        for team in teams:
            alt = team.get('alt')
            if alt not in Teams:
                Teams.append(alt)

        ### START THE CRAWLER ###

        links=[]
        for team in teams:
            link = team.get('href')
            if link not in links:
                links.append(link)


        self.starting_eleven=[]
        for url2 in links:
            html2 = urllib.request.urlopen(url2)
            soup2 = BeautifulSoup(html2, features="lxml")
            team_ = soup2('span', class_='nombre')
            team_ = re.findall('(?<=>).*(?=<)', str(team_))
            jug = soup2('a', class_='juggador')
            player_data=[]
            for i in jug:
                player_data.append(i.contents)
                p = re.findall('\d\d%',str(i.contents))
                n = re.findall('(?<=>).*(?=<)',str(i.contents))
                names = []
                for name in self.starting_eleven:
                    names.append(name[0])
                if len(n)>0:
                    if n[0] not in names:
                        if p != []:
                            z = [n[0], p[0], team_[0]]
                            self.starting_eleven.append(z)

        self.starters = pd.DataFrame(self.starting_eleven, columns=['Name', 'Chance', 'Team'])

        # Get the starting eleven chances:
    def get_starting_eleven(self, team):
        #for i, j, k in self.starters.get(self.starters['Team'] == team).values:
            #print("{}: {}".format(i, j))

        return self.starters.get(self.starters['Team'] == team)

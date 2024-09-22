
from bs4 import BeautifulSoup
import pandas as pd
import requests
from FutbolFantasy.const import FUTBOLFANTASY_URL
from pydantic import BaseModel
import logging

lg = logging.getLogger(__name__)

class Player(BaseModel):
    name: str
    team: str
    href: str
    yellow_cards: int
    red_cards: int
    injury: float
    matches: int
    start_probability: int
    goals: int
    assists: int
    picas: int
    picas_per_game: float
    futmondo_stats_total: int
    futmondo_stats_per_match: float
    cope_average_grade: float
    as_stats_total: int
    as_stats_per_match: float


class Team(BaseModel):
    name: str
    href: str
    roaster: list[Player]

    def __str__(self) -> str:
        return self.name

class Fetcher:
    def __init__(self) -> None:
        self.html_data = requests.get(
            url=FUTBOLFANTASY_URL, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",}
        )
        self.soup = BeautifulSoup(self.html_data.text, "lxml")

    def teams(self):
        for team in self.soup.find(class_="teams liga").children:
            if len(str(team)) > 10:
                soup = BeautifulSoup(requests.get(team['href']).text, "lxml")
                players_ = soup.findAll("a", class_ = "camiseta")
                players=[]
                lg.info(team['alt'])
                for x in players_:
                    
                    try:
                        players.append(Player(
                            name= x.get('href', None).replace(FUTBOLFANTASY_URL+'jugadores/', '').replace('-',' '),
                            team = team['alt'],
                            href = x.get('href', None),
                            yellow_cards = x.get('data-totalamarillas', 0),
                            red_cards = x.get('data-totalrojas', 0),
                            injury = x.get('data-lesion', 0),
                            matches = x.get('data-totalpartidosjugados', 0),
                            start_probability = int(x.get('data-probabilidad', '0%').replace('%', '')),
                            goals = x.get('data-totalgoles', 0),
                            assists = x.get('data-totalasistencias',0),
                            picas = x.get('data-totalpicas', 0),
                            picas_per_game = float(x.get('data-totalpicaspartido', '0').replace('', '0')),
                            futmondo_stats_total = x.get('data-totalpuntosfutmondostats', 0),
                            futmondo_stats_per_match = x.get('data-totalpuntosfutmondostatspartido', 0),
                            cope_average_grade = x.get('data-totalnotacopepartido', 0),
                            as_stats_total = x.get('data-totalpuntosfutmondomixtoas', 0),
                            as_stats_per_match = x.get('data-totalpuntosfutmondomixtoaspartido', 0),

                        ))
                    except:
                        continue
                yield Team(name=team['alt'], href=team['href'], roaster=players)

    def get_df(self) -> pd.DataFrame:
        df = pd.DataFrame()
        for team in self.teams():
            for player in team.roaster:
                df = pd.concat([df, pd.DataFrame({k: [v] for k, v in dict(player).items()})])
        return df
    
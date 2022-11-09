import pandas as pd
import requests
import json

class Sscore:
    def __init__(self, rapidapi_host, rapidapi_key):
        self.ids=[]
        self.team_ids=dict()
        self.url = "https://divanscore.p.rapidapi.com/"
        self.Sofascore=pd.DataFrame(columns=['Jugador','Media','Equipo','ID'])
        self.headers = {
                    'x-rapidapi-host': rapidapi_host,
                    'x-rapidapi-key': rapidapi_key
                    }

    def get_player_ratings(self, name):
        """Under Development"""
        querystring = {'name': name}
        url = self.url + "players/search"

        r = requests.request("GET", url, headers = self.headers,
                                params = querystring)
        basic_data = r.json()
        id = basic_data['players'][0]['id']
        tournament_id = basic_data['players'][0]['team']['primaryUniqueTournament']['id']
        url = self.url + "players/get-statistics-seasons"
        querystring = {"playerId":str(id)}
        r = requests.request("GET", url, headers=self.headers,
                             params = querystring)
        stats_data = r.json()
        season_id = stats_data['uniqueTournamentSeasons'][0]['seasons'][0]['id']

        url = self.url + "players/get-last-ratings"
        querystring = {"playerId":str(id),"tournamentId":str(tournament_id),"seasonId":str(season_id)}

        r = requests.request("GET", url, headers=self.headers,
                             params = querystring)
        last_stats = r.json()
        avg = 0
        for i in range (5):
            point = float(last_stats['lastRatings'][i]['rating'])
            avg += (point/5)
            against = last_stats['lastRatings'][i]['opponent']['name']
            print(
                "Against: "+against,
                " - ",point
            )
        print(avg)


#ss = Sscore(rapidapi_key="xxxxxx", rapidapi_host="divanscore.p.rapidapi.com")
#ss.get_player_ratings("Luka Modric")
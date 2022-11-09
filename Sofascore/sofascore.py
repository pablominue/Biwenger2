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
        print(r.text)
        basic_data = r.json()
        id = basic_data['players'][0]['id']
        tournament_id = basic_data['players'][0]['team']['tournament']['id']
        print(id)
        url = self.url + "/players/get-statistics-seasons"
        _querystring = {"playerId":str(id)}
        r = requests.request("GET", url, headers=self.headers,
                             params = _querystring)
        print(r.text)
        stats_data = r.json()
        print("stats: ",stats_data, "\n",
              "Torunament Id: ", tournament_id)

        print (id)

ss = Sscore(rapidapi_key="de16afdbbbmsh88b8fd071513f1dp12be45jsndfb35da30901",
            rapidapi_host="divanscore.p.rapidapi.com")
ss.get_player_ratings("Luka Modric")
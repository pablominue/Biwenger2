from Biwenger import Data
from FutbolFantasy import Fetcher
from fuzzywuzzy import process
import pandas as pd
from flask import Flask

app = Flask(__name__)

def match_names(name, choices, scorer, threshold=45):
    match, score = process.extractOne(name, choices, scorer=scorer)
    return match if score >= threshold else None

class Api:
    def __init__(self) -> None:
        self.ff = Fetcher()
        self.bw = Data()

    def join_data(self) -> None:
        ff_df = self.ff.get_df()
        choices = ff_df['name'].tolist()
        self.bw.data['name'] = self.bw.data['name'].apply(lambda x: x.lower())
        self.bw.data['matched_name'] = self.bw.data['name'].apply(lambda x: match_names(x, choices, process.fuzz.token_sort_ratio))

        df = pd.merge(self.bw.data, ff_df, left_on='matched_name', right_on='name', how='left')
        n = len(df.loc[df.name_y.isna()])
        print(f"{n} results not found of {len(df)}")
        return df

    def get_biwenger_data(self) -> pd.DataFrame:
        return self.bw.data
    
    def get_futbol_fantasy_data(self) -> pd.DataFrame:
        return self.ff.get_df()
    
bot = Api()

@app.route("/biwenger")
def get_biwenger_data():
    return bot.get_biwenger_data().to_json()

@app.route("/futbolfantasy")
def get_futbolfantasy_data():
    return bot.get_futbol_fantasy_data().to_json()
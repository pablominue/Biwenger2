from Biwenger import biwenger as bw
from FutbolFantasy import ff

data = bw.Data()
starters = ff.Starters()

def profit_chance(type):
    pack = bw.Pack(type,
                   data.data)
    chance = pack.profit_chance()
    return chance

def player_performance(name):
    player = bw.Player(data.data,
                       name)
    performance = player.profitability
    return performance

def start_eleven(team):
    team_starters = starters.get_starting_eleven(team)
    starters_list = []
    for i in range (len(team_starters)):
        try:
            row = team_starters.iloc[[i]]
            starters_list.append([row['Name'][i],row['Chance'][i]])
        except:
            break

    return starters_list

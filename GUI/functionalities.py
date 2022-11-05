from Biwenger import biwenger as bw

data = bw.Data()

def profit_chance(type):
    pack = bw.Pack(type,
                   data.data)
    chance = pack.profit_chance()
    return chance
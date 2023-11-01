from nba_api.stats.static import teams
import matplotlib.pyplot as plt
import pandas as pd
from nba_api.stats.endpoints import leaguegamefinder

def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict 

nba_teams = teams.get_teams()
#print(nba_teams)
nba_teams[0:3]
#print(nba_teams[0:3])
dict_nba_team = one_dict(nba_teams)
df_teams = pd.DataFrame(nba_teams)
df_teams.head()

#print(df_teams.head())

df_warriors=df_teams[df_teams['nickname']=='Warriors']
print(df_warriors)

id_warriors=df_warriors[['id']].values[0][0]
# we now have an integer that can be used to request the Warriors information 
print(id_warriors)


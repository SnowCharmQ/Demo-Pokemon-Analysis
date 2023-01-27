import pandas as pd
from tqdm import tqdm
from urllib import request
from urllib.request import Request

headers = {'User-Agent': 'Mozilla/5.0 3578.98 Safari/537.36'}
pokemon_df = pd.read_csv("../data/pokemon.csv")
pokemons = []
for index, row in pokemon_df.iterrows():
    idx = row['id']
    name = row['name']
    if (idx, name) not in pokemons:
        pokemons.append((idx, name))
for pokemon in tqdm(pokemons):
    name = pokemon[1]
    url = "https://pokemondb.net/pokedex/{}".format(name)
    url = Request(url, headers=headers)
    res = request.urlopen(url)
    html = res.read()
    html = html.decode()

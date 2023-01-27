import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup
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
    soup = BeautifulSoup(html, features="lxml")
    div = soup.find("div", attrs={"class": "sv-tabs-tab-list"})
    aa = div.find_all("a", attrs={"class": "sv-tabs-tab"})
    labels = [a.text for a in aa]
    sv_tabs = soup.find("div", attrs={"class": "sv-tabs-panel-list"})
    sv_tabs_divs = sv_tabs.find_all("div", attrs={"class": "sv-tabs-panel"})
    for sv_div in sv_tabs_divs:
        grid_cols = sv_div.find_all("div", attrs={"class": "grid-col"})

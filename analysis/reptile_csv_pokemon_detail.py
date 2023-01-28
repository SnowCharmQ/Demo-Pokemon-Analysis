import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup
from collections import defaultdict
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

details = defaultdict(list)


def modify_name(pokemon_name):
    if pokemon_name == "Nidoran♀":
        pokemon_name = "Nidoran-f"
    if pokemon_name == "Nidoran♂":
        pokemon_name = "Nidoran-m"
    pokemon_name = pokemon_name.replace("'", "")
    pokemon_name = pokemon_name.replace(" ", "-")
    return pokemon_name


def analysis(html, idx, name):
    soup = BeautifulSoup(html, features="lxml")
    div = soup.find("div", attrs={"class": "sv-tabs-tab-list"})
    aa = div.find_all("a", attrs={"class": "sv-tabs-tab"})
    type_cnt = len(aa)
    labels = [a.text for a in aa]
    labels.reverse()
    sv_tabs = soup.find("div", attrs={"class": "sv-tabs-panel-list"})
    sv_tabs_divs = sv_tabs.find_all("div", attrs={"class": "sv-tabs-panel"})
    for sv_div in sv_tabs_divs:
        grid_cols = sv_div.find_all("div", attrs={"class": "grid-col"})
        if len(grid_cols) != 7:
            continue

        col0 = grid_cols[0]
        item = col0.select("p a")
        img = item[0].get("href")

        col1 = grid_cols[1]
        trs = col1.find_all("tr")
        tr1 = trs[1]
        tds = tr1.find("td")
        types = [t.text for t in tds if t.text.strip() != '']
        tr2 = trs[2]
        species = tr2.find("td").text
        tr3 = trs[3]
        height = tr3.find("td").text
        tr4 = trs[4]
        weight = tr4.find("td").text
        tr5 = trs[5]
        aas = tr5.find_all("a")
        abilities = [a.text for a in aas]
        abilities = ' | '.join(abilities)

        col4 = grid_cols[4]
        trs = col4.find_all("tr")
        tr0 = trs[0]
        aas = tr0.find_all("a")
        eggs = [a.text for a in aas]
        tr1 = trs[1]
        td = tr1.find("td")
        gender = td.text

        col5 = grid_cols[5]
        trs = col5.find_all("tr")
        stats = {}
        for i in range(6):
            tr = trs[i]
            th = tr.find("th").text
            td = tr.find("td").text
            stats[th] = int(td)
        total = sum(stats.values())

        resp_scroll = sv_div.find("div", attrs={"class": "resp-scroll text-center"})
        trs = resp_scroll.find_all("tr")
        defenses = []
        ths1 = trs[0].find_all("th")
        ths2 = trs[2].find_all("th")
        ths = ths1 + ths2
        for th in ths:
            defenses.append(th.text)
        effects = []
        tds1 = trs[1].find_all("td")
        tds2 = trs[3].find_all("td")
        tds = tds1 + tds2
        for td in tds:
            num = td.text if td.text != '' else '1'
            effects.append(num)
        label = labels.pop()
        details['type_cnt'].append(type_cnt)
        details['label'].append(label)
        details['img'].append(img)
        if len(types) == 2:
            details['type1'].append(types[0])
            details['type2'].append(types[1])
        else:
            details['type1'].append(types[0])
            details['type2'].append('')
        details['species'].append(species)
        details['height'].append(height)
        details['weight'].append(weight)
        details['abilities'].append(abilities)
        details['eggs'].append(eggs)
        details['gender'].append(gender)
        for item in stats.items():
            details[item[0]].append(item[1])
        details['total'].append(total)
        for i in range(18):
            details[defenses[i]].append(effects[i])


for pokemon in tqdm(pokemons):
    idx = pokemon[0]
    name = pokemon[1]
    name = modify_name(name)
    url = "https://pokemondb.net/pokedex/{}".format(name)
    url = Request(url, headers=headers)
    res = request.urlopen(url)
    html = res.read()
    html = html.decode()
    analysis(html, idx, name)
df = pd.DataFrame(details)
df.to_csv("../data/pokemon_details.csv", index=False)

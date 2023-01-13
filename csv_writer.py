import pandas as pd
from bs4 import BeautifulSoup

pokemons = []
soup = BeautifulSoup(open("data/pokemon.html", mode='r', encoding='utf-8'), features="lxml")
trs = soup.find_all('tr')
for tr in trs:
    info = []
    tds = tr.find_all('td')
    for i in range(len(tds)):
        td = tds[i]
        text = td.text.strip()
        if i == 0 and not text.isdigit():
            break
        if text:
            info.append(text)
    if len(info) == 5:
        info = [info[0], info[1], info[2], '', info[3], info[4]]
    if len(info) == 6:
        pokemons.append(info)

df = pd.DataFrame(pokemons, columns=['id', 'english_name', 'japanese_name', 'type1', 'type2', 'official_rom'])
df.to_csv('data/pokemon.csv', index=False)

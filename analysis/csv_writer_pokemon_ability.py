import pandas as pd
from bs4 import BeautifulSoup

pokemons = []
soup = BeautifulSoup(open("../data/pokemon_ability.html", mode='r', encoding='utf-8'), features="lxml")
trs = soup.find_all('tr')

for tr in trs:
    info = []
    tds = tr.find_all('td')
    flag = False
    for i in range(len(tds)):
        td = tds[i]
        text = td.text.strip()
        if i == 0 and text.isdigit():
            idx = int(text)
            info.append(idx)
            continue
        if i == 1:
            continue
        small = td.small
        small = small.text.strip() if small is not None else ''
        if not flag and small != '':
            if "Mega" in small:
                break
            text = text.replace(small, '')
            info.append(text)
            info.append(small)
            flag = True
            continue
        elif not flag and small == '':
            info.append(text)
            info.append('')
            flag = True
            continue
        info.append(text)
    if len(info) == 6:
        pokemons.append(info)

sorted(pokemons, key=lambda x: x[0])
df = pd.DataFrame(pokemons, columns=['id', 'name', 'detail',
                                     'ability1', 'ability2',
                                     'hide_ability'])
df.to_csv('../data/pokemon_ability.csv', index=False)

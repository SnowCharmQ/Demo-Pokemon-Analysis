import pandas as pd
from bs4 import BeautifulSoup

url = "https://bulbapedia.bulbagarden.net"
pokemons = []
soup = BeautifulSoup(open("../data/pokemon.html", mode='r', encoding='utf-8'), features="lxml")
trs = soup.find_all('tr')
idx = 0
for tr in trs:
    info = []
    tds = tr.find_all('td')
    flag1, flag2 = False, False
    for i in range(len(tds)):
        td = tds[i]
        text = td.text.strip()
        num = td.text.strip().replace("#", "")
        if i == 0 and num.isdigit():
            idx = int(num)
            info.append(idx)
            continue
        elif i == 0 and idx != 0 and idx < 1008:
            info.append(idx)
        a = td.a
        href = a.get('href') if a is not None else ''
        if not flag1 and href != '':
            info.append(url + str(href))
            flag1 = True
            continue
        small = td.small
        small = small.text.strip() if small is not None else ''
        if not flag2 and small != '':
            text = text.replace(small, '')
            info.append(text)
            info.append(small)
            flag2 = True
            continue
        elif not flag2 and small == '':
            info.append(text)
            info.append('')
            flag2 = True
            continue
        info.append(text)
    if len(info) == 5:
        info.append('')
    if len(info) == 6:
        pokemons.append(info)

df = pd.DataFrame(pokemons, columns=['id', 'href', 'name', 'detail', 'type1', 'type2'])
df.to_csv('../data/pokemon.csv', index=False)

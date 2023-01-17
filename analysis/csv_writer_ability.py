import pandas as pd
from bs4 import BeautifulSoup

abilities = []
soup = BeautifulSoup(open("../data/ability.html", mode='r', encoding='utf-8'), features='lxml')
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
    if len(info) == 4:
        abilities.append(info)

df = pd.DataFrame(abilities, columns=['id', 'name', 'description', 'gen'])
df.to_csv('../data/ability.csv', index=False)

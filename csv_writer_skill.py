import pandas as pd
from bs4 import BeautifulSoup

skills = []
soup = BeautifulSoup(open("data/skill.html", mode='r', encoding='utf-8'), features='lxml')
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
    if len(info) == 8:
        skills.append(info)

df = pd.DataFrame(skills, columns=['id', 'name', 'type', 'category', 'pp', 'power', 'accuracy', 'gen'])
df.to_csv('data/skill.csv', index=False)

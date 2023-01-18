import os
from urllib import request
from urllib.request import Request

url = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_Ability"
headers = {'User-Agent': 'Mozilla/5.0 3578.98 Safari/537.36'}
url = Request(url, headers=headers)
res = request.urlopen(url)

html = res.read()
html = html.decode()

if not os.path.exists('../data'):
    os.makedirs('../data')
with open("../data/pokemon_ability.html", mode='w', encoding='utf-8') as f:
    f.write(html)
f.close()

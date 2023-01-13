import os
from urllib import request

url = "https://pokemon.fandom.com/wiki/List_of_Pok%C3%A9mon"
res = request.urlopen(url)

html = res.read()
html = html.decode()

if not os.path.exists('data'):
    os.makedirs('data')
with open("data/pokemon.txt", mode='w', encoding='utf-8') as f:
    f.write(html)
f.close()

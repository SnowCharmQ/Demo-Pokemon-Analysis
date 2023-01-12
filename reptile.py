from urllib import request

url = "https://pokemon.fandom.com/wiki/List_of_Pok%C3%A9mon"
res = request.urlopen(url)

html = res.read()
print(html)

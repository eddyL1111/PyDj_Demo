import requests
from bs4 import BeautifulSoup

def get_lol_champs0():
	lol_url = "http://leagueoflegends.wikia.com/wiki/League_of_Legends_Wiki"
	source_code = requests.get(lol_url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text, "html.parser")
	champions_found = soup.findAll('div', {'class': 'character_icon'})
	champions = []

	for data in champions_found:
		context = {
			'name': data.get('data-character'),
			'icon_url': data.a.img.get('data-src')
		}
		champions.append(context)
	
	return champions
	
def get_lol_champs():
    lol_url = "http://leagueoflegends.wikia.com/wiki/League_of_Legends_Wiki"
    source_code = requests.get(lol_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    champs_soup = soup.findAll('div', {'id': 'champions'})
    result = []

    for champ in champs_soup:
        roster_soup = champ.findAll('div', {'id': 'roster'})
        rotation_soup = champ.findAll('div', {'id': 'rotation'})

        for roster in roster_soup:
            item_soup = roster.findAll('li')
            temp = []
            for item in item_soup:
                data = {
                    'name': item.span.get('data-character'),
                    'icon_url': item.span.a.img.get('data-src')
                }
                temp.append(data)
            result.append(temp)

        for rotation in rotation_soup:
            item_soup = rotation.findAll('li')
            temp = []
            for item in item_soup:
                data = {
                    'name': item.span.get('data-character'),
                    'icon_url': item.span.a.img.get('data-src')
                }
                temp.append(data)
            result.append(temp)

    return result
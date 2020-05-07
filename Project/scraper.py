import requests
from bs4 import BeautifulSoup

BASE_URL = "https://en.wikipedia.org/"
URL = BASE_URL + "wiki/Member_states_of_the_United_Nations"

# Dictionary of HTTP headers
headers = {'User-Agent': f'Your name (your@email.com)'}
response = requests.get(URL, headers=headers)
assert response.status_code == 200

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', attrs={'class': 'wikitable'})

print(table.caption.string)

rows = table.tbody.find_all('tr')

country_list = []
for row in rows:
    country_name_th = row.find('th', attrs={'scope': 'row'})
    if country_name_th:
        country_name = country_name_th.a.string
        print(country_name)
        country_list.append(country_name)


with open('countries.txt', 'w') as file:
    for country in country_list:
        file.write(country + '\n')

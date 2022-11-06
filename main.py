from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    "Content-Type": "application/x-www-form-urlencoded"}

url = 'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating'

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())

movies = soup.find_all('div', class_ = 'lister-item-content')

for movie in movies:
    rank = movie.find('span', class_="lister-item-index unbold text-primary")
    title = movie.find("a")
    movie_url = 'https://www.imdb.com' + title['href']
    year = movie.find('span', class_="lister-item-year text-muted unbold")
    description = movie.find_all("p", class_="text-muted")[1]
    data = movie.find('p', class_="")
    data = data.text.strip().replace("\n","")
    data_array = data.split('|')
    director = data_array[0].split(':')[1]
    stars = data_array[1].split(':')[1]
    print(f'{rank.text.strip()} {title.text.strip()} {year.text.strip()}')
    print(description.text.strip())
    print(f'Director: {director}')
    print(f'Stars: {stars}')
    print(f'IMDb Link: {movie_url}')
    print()
    
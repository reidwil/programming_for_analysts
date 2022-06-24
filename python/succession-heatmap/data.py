import requests
from bs4 import BeautifulSoup
import pandas as pd

def generate_seasons(seasons):
    base_url = 'https://www.imdb.com/title/tt7660850/episodes?season='
    urls = []
    for season in range(seasons):
        urls.append(base_url + str(season+1))
    return urls

class Episodes:
    def __init__(self, url):
        self.url = url
        self.titles = []
        self.air_dates = []
        self.ratings = []
        self.votes = []
        self.season = []

    def soupify(self) -> BeautifulSoup:
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    
    def get_episodes(self):
        soup = self.soupify()
        episodes = soup.find_all('div', class_='info')
        return episodes
    
    def populate_data(self):
        episodes = self.get_episodes()
        for episode in episodes:
            # I hate the specificity of bs4/html here
            self.titles.append(episode.a['title'])
            self.air_dates.append(episode.find('div',class_='airdate').text.strip())
            self.ratings.append(float(episode.find('span', class_='ipl-rating-star__rating').text))
            self.votes.append(episode.find('span', class_='ipl-rating-star__total-votes').text)
        return list(zip(self.titles, self.air_dates, self.ratings, self.votes))

def main():
    seasons = []
    columns = ['Title','Release Date','Rating','Votes']
    for url in generate_seasons(3):
        season = Episodes(url)
        season_data = season.populate_data()
        seasons.append(pd.DataFrame(season_data, columns=columns))
    df = pd.concat(seasons)
    df.to_csv('results.csv', index=False)

if __name__=='__main__':
    main()
import requests
import json

class api():
  
    def __init__(self):
        self.apiKey = open('apiKey.json', 'r')
        self.data_URL = 'http://www.omdbapi.com/?apikey={}'.format(self.apiKey.read())
    
    def by_search(self, title, prod_type='movie',year=''):
        params = {
            's':title,
            'type':prod_type, #type to specify as an argument in method call: movie/series/episode
            'y': year
        }
        response = requests.get(self.data_URL,params=params).json()
        with open('search_results.json', 'w') as f:
            json.dump(response, f)

    def by_title(self, title, prod_type='movie',year=''):
        params = {
            't':title,
            'type':prod_type, #type to specify as an argument in method call: movie/series/episode
            'y': year
        }
        response = requests.get(self.data_URL,params=params).json()
        with open('title_results.json', 'w') as f:
            json.dump(response, f)

if __name__ == '__main__':

    a = api()
    a.by_search('supernatural', 'series')
    a.by_title('supernatural', 'series')


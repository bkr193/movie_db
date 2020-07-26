import requests
import json

class api():
  
    def __init__(self):
        self.apiKey = open('apiKey.json', 'r')
        self.data_URL = 'http://www.omdbapi.com/?apikey={}'.format(self.apiKey.read())

class search_api(api):

    
    def __init__(self):
        pass

    def search_movie(self, title):
        params = {
            's':title,
            'type':'movie',
        }
        response = requests.get(self.data_URL,params=params).json()
        with open('search_results.json', 'w') as f:
            json.dump(response, f)

if __name__ == '__main__':

    a = api()
    a.search_movie('harry potter')


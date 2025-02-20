import requests 
import os


API_KEY = os.environ['TASK2APIKEY']

response = requests.get(f'https://newsapi.org/v2/top-headlines?category=science&apiKey={API_KEY}')
if response.ok:
    print('These are 5 top science-related news articles:')
    for i in range(5):
        current_article = response.json()['articles'][i]
        print()
        print(f'Title: {current_article['title']}')
        print(f'Author: {current_article['author'] if current_article['author'] != None else 'Not stated'}')
        print(f'Url: {current_article['url']}')
        print(f'Date: {current_article['publishedAt']}')


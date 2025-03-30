import requests
import json


API_KEY = "10e3c47db0db4d25bd58fbcc71f0648b"
URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"


def extract():
    """ Fucntion to extract data from news api"""

    row_data = []

    try:
        response = requests.get(url= URL)

        if response.status_code == 200:
            data = response.json()
            articles = data["articles"]
            for i in range(len(articles)):
                row_data.append({
                                'source_name':articles[i]["source"]["name"],
                                'author': articles[i].get("author", articles[i]["source"]["name"]),
                                'title': articles[i]["title"],
                                'description': articles[i].get('description', 'No description'),
                                'url': articles[i]["url"],
                                'published_at': articles[i]['publishedAt']
                                })
        
        else:
            print('Error Fetching Data', response.status_code)
            return[]
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

    
    return row_data




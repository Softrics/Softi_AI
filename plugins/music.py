import os
import requests
import json

def fetch(song):
    
    url = "https://youtube-search-and-download.p.rapidapi.com/search"

    querystring = {"query":song,"type":"video","limit":"1","gl":"IN"}

    headers = {
        'x-rapidapi-host': "youtube-search-and-download.p.rapidapi.com",
        'x-rapidapi-key': os.environ.get('VOICE_API_KEY')
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    result=json.loads(response.text)
    id=result['contents'][0]['video']['videoId']
    return play(id)
def play(id):
    url = "https://youtube-mp36.p.rapidapi.com/dl"

    querystring = {"id":id}

    headers = {
        'x-rapidapi-host': "youtube-mp36.p.rapidapi.com",
        'x-rapidapi-key': os.environ.get('VOICE_API_KEY')
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    result=json.loads(response.text)
    return result["link"]

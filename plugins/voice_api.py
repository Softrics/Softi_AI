import requests
import os
import json
def voiceApi(command):
    url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"

    querystring = {"bid":"178","key":"sX5A2PcYZbsN5EY6","uid":"mashape","msg":command}

    headers = {
        'x-rapidapi-host': "acobot-brainshop-ai-v1.p.rapidapi.com",
        'x-rapidapi-key': os.environ.get('VOICE_API_KEY')
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    result=json.loads(response.text)
    return result['cnt']
import requests
import os
import json
def voiceApi(command):
    url = "http://api.brainshop.ai/get"

    querystring = {"bid":"163338","key":os.environ.get("BRAIN_KEY"),"uid":"mashape","msg":command}

    headers = {
        'x-rapidapi-host': "acobot-brainshop-ai-v1.p.rapidapi.com",
        'x-rapidapi-key': os.environ.get('VOICE_API_KEY')
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    result=json.loads(response.text)
    if result['cnt']=='':
        return "Sorry, I am still learning, I will answer this soon!"
    return result['cnt']
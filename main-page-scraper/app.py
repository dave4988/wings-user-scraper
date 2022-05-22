import requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):

    try:
        url = "https://www.wingsxi.com/wings/index.php?page=onlineusers"
        req = requests.get(url)
        soupObject = BeautifulSoup(req.text, "html.parser")
        
        characters = soupObject.find_all("tr", class_ = "character")
        print('got characters: ', characters)
        print(characters)

        return {
            'characters': characters
        }

    except requests.RequestException as e:
        print(e)
        raise e
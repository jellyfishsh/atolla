import requests
import json

def randomDuckImg() -> str:
    x = requests.get("https://random-d.uk/api/random").text
    y = json.loads(x)
    return y["url"]

def randomBunnyGif():
    x = requests.get("https://api.bunnies.io/v2/loop/random/?media=gif").text
    y = json.loads(x)
    return y

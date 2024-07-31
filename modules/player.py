import random
import requests


headers = {
  'Accept': 'application/json'
}

def getClass():
    classes = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"];
    return(random.choice(classes));
    
def getClassInformation(selectedClass):
    response = requests.request("GET", f"https://www.dnd5eapi.co/api/classes/{selectedClass}/levels")

    return (response.text)
    
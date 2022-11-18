import json
import time
from time import sleep

with open ("Initialisation.json", "r") as jsonFile : 
    infosJson = json.load(jsonFile)

#Elements à remplir/Initialisation de la requête :
identifiantInsta = infosJson["identifiantInsta"] 
mdpInsta = infosJson["mdpInsta"] 
hashtag_choisi = infosJson["hashtag_choisi"] 
min_abon = infosJson["min_abon"]  
max_abon = infosJson["max_abon"] 
print(identifiantInsta, mdpInsta, hashtag_choisi, min_abon, max_abon)

sleep(15)
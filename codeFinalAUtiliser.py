"""
⚠️ NE RIEN TOUCHER DANS LE CODE !!!! ⚠️
"""
import random
import time
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import (ElementClickInterceptedException,
                                        NoSuchElementException,
                                        StaleElementReferenceException,
                                        TimeoutException)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from tabulate import tabulate
from datetime import datetime
import csv
import sys 
import json

print("Test")
sleep(10)

sys.stdout=open("Logs.log", "a" )

with open ("Initialisation.json", "r") as jsonFile : 
    infosJson = json.load(jsonFile)

#Elements à remplir/Initialisation de la requête :
identifiantInsta = infosJson["identifiantInsta"] 
mdpInsta = infosJson["mdpInsta"] 
hashtag_choisi = infosJson["hashtag_choisi"] 
min_abon = infosJson["min_abon"]  
max_abon = infosJson["max_abon"] 


data = []

driver = webdriver.Chrome ()
options = Options ()
options . headless = True

#Début Exécution Script
driver.get ("https://www.instagram.com")
driver.maximize_window()
sleep(5)

print("Début Test")

#Accepter les cookies
if driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]") : 
     driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]").click()
sleep(2)

#Le bot va entrer les identifiants
headless_browser = True 
username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")

username_input.send_keys(identifiantInsta)
password_input.send_keys(mdpInsta)

sleep(2)

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
sleep(10)
#Fin Login

#Enregistrer les identifiants : 
if driver.find_element(By.XPATH, "//button[@class='_acan _acao _acas']") :
    driver.find_element(By.XPATH, "//button[@class='_acan _acao _acas']").click()
sleep(2)

#Notifications 
if driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]") : 
     driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
sleep(3)

#Choisir le hashtag à utiliser
print (hashtag_choisi)
driver.get ("https://www.instagram.com/explore/tags/" + hashtag_choisi + "/")
sleep(10)


def obtainNbrFollowers (str_followers) :
    if "," or "K" in str_followers : 
        print("Le nbr de followers contient des virgules ou la lettre K")
        new_string_followers = str_followers.replace(",", ".").replace("K", "")
        print(new_string_followers)
        str_to_float = float(new_string_followers)
        print(str_to_float)
        nbr_followers = str_to_float * 1000
        print(f'Nbr x 1000 : {nbr_followers}')
        return nbr_followers
    elif "M" in str_followers : 
        new_string_followers = str_followers.replace("M", "")
        nbr_followers = str_to_float * 1000
        print(f'Nbr x 1Million : {nbr_followers}')
        return nbr_followers
    else :
        nbr_followers = int(str_followers)
        return nbr_followers

#Cliquer sur chaque poste 
def main () : 
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    i = 0
    while i < 200 : 
        action = ActionChains(driver)
        liens_post = []
        with open('resultatsBot.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ',
                                    quoting=csv.QUOTE_MINIMAL)
            liens_post = driver.find_elements(By.XPATH, "//div[contains(@class,'_aagu')]")
            for lien in liens_post :
                list = []
                action.click(lien)
                sleep(5)
                action.perform()
                WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/div/span/a")))
                nomProfil = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/div/span/a").get_attribute("innerText")
                print(nomProfil)
                #list.append(nomProfil)
                lien_profil = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/div/span/a").get_attribute("href")
                print(lien_profil)

                #Open New Tab
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[1])
                driver.get(lien_profil)
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/div/span")))
                str_followers = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/div/span").get_attribute("innerText")
                print(f"{nomProfil} et String issu d'Instagram : {str_followers}")
                nbr_followers = obtainNbrFollowers (str_followers) 
                print(f"{nomProfil} : nbr_followers")
                if  min_abon <= nbr_followers <= max_abon :
                    print(f"{nomProfil} : Assez d'abonnés")
                    list.append(nomProfil)
                    list.append(lien_profil)
                    list.append(nbr_followers)
                    print(f"{nomProfil} : {list}")
                    writer.writerow(list)
                    data.append(list)
                    print(f"{nomProfil} : {data}")
                    i+=1
                    print (i)
                
                else :
                    print(f"{nomProfil} : Pas dans la range d'abonnés")
                
                driver.close()
                #Fin New Tab
                
                sleep(2)
                driver.switch_to.window(driver.window_handles[0])
                action.send_keys(Keys.ESCAPE)
                print(data)
                action.scroll_by_amount(0,150)

#Lancer le main
main()







"""
if "," or "K"or "M" in str_followers : 
                print("Le nbr de followers contient des virgules ou la lettre K")
                new_string_followers = str_followers.replace(",", ".").replace("K", "").replace("M", "")
                print(new_string_followers)
                str_to_float = float(new_string_followers)
                print(str_to_float)
                nbr_followers = str_to_float * 1000
                print(f'Nbr x 1000 : {nbr_followers}')
            elif "M" in str_followers : 
                new_string_followers = str_followers.replace("M", "")
                nbr_followers = str_to_float * 1000
                print(f'Nbr x 1Million : {nbr_followers}')
            else :
                nbr_followers = int(str_followers)
"""

















"""
for lien in liens_post :
    lien.click()
    sleep(20)
"""
#driver.find_element(By.CLASS_NAME, liens_post[1]).click()
#sleep(5)
"""
i = 0
while i < 6 :
    action.click(liens_post[i])
    sleep(5)
    action.send_keys(Keys.ESCAPE)
    action.perform()
    sleep(5)
    i+=1

sleep(20)
"""




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
import csv

#Initialize CSV
"""file = open('exemple.csv', 'w',  newline='') 
writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL, delimiter=',')"""


data = []

driver = webdriver.Chrome ()
options = Options ()
options . headless = True

#Début Exécution Script
driver.get ("https://www.instagram.com")
driver.maximize_window()
sleep(10)

print("Début Test")

#Accepter les cookies
if driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]") : 
     driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]").click()
sleep(2)

#Entrer ses identifiants
headless_browser = True 
username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")

username_input.send_keys("sagesse_d_athena") #A remplacer par input
password_input.send_keys("Ads'eisie21!")

sleep(2)

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
sleep(10)
#Fin Login

#Notifications 
if driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]") : 
     driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()

sleep(3)

#Choisir le hashtag à utiliser
hashtag_choisi = "automatisation"
print (hashtag_choisi)
driver.get ("https://www.instagram.com/explore/tags/" + hashtag_choisi + "/")
sleep(10)

#Cliquer sur un post
#driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[1]/div[1]").click()
#sleep(20)

#Trouver les liens des profils
#liens_post = driver.find_elements(By.CSS_SELECTOR, a[class =''])
#all_children_by_xpath = liens_post.find_element(By.XPATH, ".//*")

#Cliquer sur chaque poste 
action = ActionChains(driver)

liens_post = []
#liens_post = driver.find_elements(By.XPATH, "//div[contains(@class,'_aabd _aa8k _aanf')]")
#(//a[contains(@class,'_acaw _a6hd')])[1]
#Add Scroll
with open('exemple.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ',
                            quoting=csv.QUOTE_MINIMAL)
    liens_post = driver.find_elements(By.XPATH, "//div[contains(@class,'_aagu')]")
    for lien in liens_post :
        list = []
        action.click(lien)
        sleep(10)
        action.perform()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/div/span/a")))
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
        print("String :" + str_followers)
        virgule = ","
        if virgule in str_followers : 
            print("Le nbr de followers contient des virgules")
            new_string_followers = str_followers.replace(",", ".")
            print(new_string_followers)
            str_to_float = float(new_string_followers)
            print(str_to_float)
            nbr_followers = str_to_float * 1000
            print("Nbr x 1000 :" + nbr_followers)
        else :
            nbr_followers = int(str_followers)

        if nbr_followers > 500 :
            print("Assez d'abonnés")
            list.append(nomProfil)
            list.append(lien_profil)
            list.append(nbr_followers)
            print(list)
            writer.writerow(list)
            data.append(list)
            print(data)
        
        else :
            print("Pas assez d'abonnés")
        
        driver.close()
        #Fin New Tab
        
        sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        action.send_keys(Keys.ESCAPE)
        print(data)
        action.scroll_by_amount(0,200)


sleep(60)

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




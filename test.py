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

driver = webdriver.Chrome ()
options = Options ()
options . headless = True

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

driver.get("https://www.instagram.com/luis_experiences/")
	
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/div/span")))
str_followers = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/div/span").get_attribute("innerText")
print(str_followers)
print(type(str_followers))
nbr_followers = int(str_followers)
print(nbr_followers)
print(type(nbr_followers))
sleep(25)
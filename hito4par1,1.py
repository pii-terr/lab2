from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random


url = "https://www.pizzahut.es/account/register"
url2 = "https://www.pizzahut.es/account-management/change-password"



driver = webdriver.Chrome("/Users/Pedro/Downloads/chromedriver_win32 (1)/chromedriver.exe")
driver.maximize_window()
driver.get("https://yopmail.com/es/email-generator")
email=driver.find_element(By.ID,"egen").text
passs=email.split('@')
driver.get(url)

unicode=["¡","¢","£","¤","¥"]
assci256=["@","#","~","¥","§","«","Æ","¼","ñ","Ñ","á","^","ø","=","(",")","’","þ","”","ß","Ð"]
subss= ["₁","ⁱ","ₕ","₉","ₘ","₊","⁼","⁽","ₔ","⁰"]
base62 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
Arabico = ["ي","و","ه","ش"]
emojis = [ "😊","😂","🤣","❤","😍","😒","👌","😘","🤷‍♂️"]
clave = ""
for i in range(14):
    a=random.choice(emojis)
    clave = f"{clave}{a}"
print(clave)

driver.find_element(By.XPATH ,'//*[@id="emailAddress"]').send_keys(email)
driver.find_element(By.XPATH ,'//*[@id="phoneNumber"]').send_keys("911111111")
driver.find_element(By.XPATH ,'//*[@id="password"]').send_keys(clave)
driver.find_element(By.XPATH ,'//*[@id="passwordConfirmation"]').send_keys(clave)

driver.find_element(By.XPATH ,'//*[@id="acceptTermsAndCondition"]').click()
driver.find_element(By.XPATH ,'//*[@id="subscriptionForNewsletter"]').click()
driver.find_element(By.XPATH ,'//*[@id="register-page"]/form/div[7]/button').click()

bd=open("usuarios_españa_hito4.txt","a")
bd.write(email+'\n'+clave+'\n')
bd.close()

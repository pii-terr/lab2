from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random

url = "https://www.pizzahut.cl/usuario/inicio"
driver = webdriver.Chrome("/Users/Pedro/Downloads/chromedriver_win32 (1)/chromedriver.exe")
driver.maximize_window()

driver.get("https://yopmail.com/es/email-generator")
email=driver.find_element(By.ID,"egen").text
pass_seed=email.split('@')
list1 = [1, 2, 3, 4, 5, 6]

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

print(pass_seed)

driver.get(url)
driver.get(url)
driver.find_element(By.XPATH ,'//*[@id="modHeadLogin"]/a[2]').click()
driver.find_element(By.XPATH ,'//*[@id="Email"]').send_keys(email)
driver.find_element(By.XPATH ,'//*[@id="FirstPhone"]').send_keys("911111111")
driver.find_element(By.XPATH ,'//*[@id="Password"]').send_keys(clave)
driver.find_element(By.XPATH ,'//*[@id="ConfirmPassword"]').send_keys(clave)

driver.find_element(By.XPATH ,'//*[@id="userRegister"]/div[5]/span[1]').click()
driver.find_element(By.XPATH ,'//*[@id="lbAcceptEmails"]').click()
driver.find_element(By.XPATH ,'//*[@id="lbAcceptSMS"]').click()
driver.find_element(By.XPATH ,'//*[@id="btRegister"]/span').click()

bd=open("usuarios_chile_hito4.txt","a")
bd.write(email+'\n'+clave+'\n')
bd.close()


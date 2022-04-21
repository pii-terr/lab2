from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By




url = "https://www.pizzahut.cl/usuario/inicio"


driver = webdriver.Chrome("/Users/Pedro/Downloads/chromedriver_win32 (1)/chromedriver.exe")
driver = webdriver.Chrome("/Users/Pedro/Downloads/chromedriver_win32 (1)/chromedriver.exe")
driver.maximize_window()
driver.get("https://yopmail.com/es/email-generator")
email=driver.find_element(By.ID,"egen").text
passs=email.split('@')
driver.get(url)
driver.get(url)
driver.find_element(By.XPATH ,'//*[@id="modHeadLogin"]/a[2]').click()
driver.find_element(By.XPATH ,'//*[@id="Email"]').send_keys(email)
driver.find_element(By.XPATH ,'//*[@id="FirstPhone"]').send_keys("911111111")
driver.find_element(By.XPATH ,'//*[@id="Password"]').send_keys("11111111")
driver.find_element(By.XPATH ,'//*[@id="ConfirmPassword"]').send_keys("11111111")

driver.find_element(By.XPATH ,'//*[@id="userRegister"]/div[5]/span[1]').click()

driver.find_element(By.XPATH ,'//*[@id="lbAcceptEmails"]').click()

driver.find_element(By.XPATH ,'//*[@id="lbAcceptSMS"]').click()

driver.find_element(By.XPATH ,'//*[@id="btRegister"]/span').click()
"""
driver.find_element(By.XPATH ,'//*[@id="EmailLogin"]').send_keys(email)

driver.find_element(By.XPATH ,'//*[@id="PasswordLogin"]').send_keys("11111111")

driver.find_element(By.XPATH ,'//*[@id="btLogin"]/span').click()
"""
driver.find_element(By.XPATH ,'//*[@id="headerLinks"]/ul/li[2]/a').click()

driver.find_element(By.XPATH ,'/html/body/div[3]/ul/li[2]').click()

driver.find_element(By.XPATH ,'//*[@id="my_account"]/div/div[2]/ul/li[2]').click()

#[@id="my_account"]/div/div[2]/ul/li[2]

driver.find_element(By.XPATH ,'//*[@id="user_new_password"]').send_keys("111111112")
driver.find_element(By.XPATH ,'//*[@id="user_confirm_password"]').send_keys("111111112")
driver.find_element(By.XPATH ,'//*[@id="changePassword"]/div/div/div').click()
driver.find_element(By.XPATH ,'//*[@id="passConfirmPopup"]').send_keys("11111111")
#//*[@id="popup"]/div[3]/p[2]/a/span
driver.find_element(By.XPATH ,'//*[@id="popup"]/div[3]/p[2]/a/span').click()



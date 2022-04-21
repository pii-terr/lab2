from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



url = "https://www.pizzahut.es/account/register"
url2 = "https://www.pizzahut.es/account-management/change-password"



driver = webdriver.Chrome("/Users/Pedro/Downloads/chromedriver_win32 (1)/chromedriver.exe")
driver.maximize_window()
driver.get("https://yopmail.com/es/email-generator")
email=driver.find_element(By.ID,"egen").text
passs=email.split('@')
driver.get(url)
#registro
#driver.find_element(By.XPATH ,'//*[@id="modHeadLogin"]/a[2]').click()
driver.find_element(By.XPATH ,'//*[@id="emailAddress"]').send_keys(email)
driver.find_element(By.XPATH ,'//*[@id="phoneNumber"]').send_keys("911111111")
driver.find_element(By.XPATH ,'//*[@id="password"]').send_keys("11111111")
driver.find_element(By.XPATH ,'//*[@id="passwordConfirmation"]').send_keys("11111111")

driver.find_element(By.XPATH ,'//*[@id="acceptTermsAndCondition"]').click()

driver.find_element(By.XPATH ,'//*[@id="subscriptionForNewsletter"]').click()

driver.find_element(By.XPATH ,'//*[@id="register-page"]/form/div[7]/button').click()
#inicio de sesion 
driver.execute_script("window.open('');")
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
driver.get(url2)

#driver.find_element(By.XPATH ,'//*[@id="user-drop-down"]/div[2]/div').click()

#driver.find_element(By.XPATH ,'/html/body/div[3]/ul/li[2]').click()

#river.find_element(By.XPATH ,'//*[@id="my_account"]/div/div[2]/ul/li[2]').click()

#[@id="my_account"]/div/div[2]/ul/li[2]

#clave nueva
driver.find_element(By.XPATH ,'//*[@id="newPassword"]').send_keys("111111112")
driver.find_element(By.XPATH ,'//*[@id="passwordConfirmation"]').send_keys("111111112")
driver.find_element(By.XPATH ,'//*[@id="account-details-form"]/div[3]/button').click()
driver.find_element(By.XPATH ,'//*[@id="password"]').send_keys("11111111")
#//*[@id="popup"]/div[3]/p[2]/a/span
driver.find_element(By.XPATH ,'//*[@id="confirm-changes-container"]/div/button[1]').click()




from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username = ["chiko6002","chikolalo99","hola"] 
password = ["chiko6002","3944lalo","holamundo"] 
i=0
for x in username:

    url = "https://www.educarchile.cl/user/login"


    driver = webdriver.Chrome("/Users/Pedro/Downloads/chromedriver_win32 (1)/chromedriver.exe")
    driver.get(url)

    driver.find_element_by_name("name").send_keys(x)
    print(password[i])
    driver.find_element_by_name("pass").send_keys(password[i])
    driver.find_element_by_name("pass").send_keys(Keys.ENTER)    
    

    #driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
    i=i+1
print("log")
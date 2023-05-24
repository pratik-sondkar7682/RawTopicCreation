from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service('C:\\Users\\Anuja\\Desktop\\python automation\\chromedriver.exe')
driver = webdriver.Chrome(service=ser_obj)
driver.get("http://demo.nopcommerce.com/register")
driver.maximize_window()

searchbox = driver.find_element(By.XPATH,'//*[@id="small-searchterms"]')

print("Displayed Status: ",searchbox.is_displayed())
print("Enabled Status: ",searchbox.is_enabled())

driver.close()
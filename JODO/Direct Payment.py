import pandas as pd
from selenium import webdriver
from selenium.common import TimeoutException, ElementNotInteractableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

start_time = time.time()
# Initialize the WebDriver
service_obj = Service("C:\\Users\\Anuja\\Desktop\\CMS Automation\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[Exception])
driver.maximize_window()

# Database
df = pd.read_csv("C:\\Users\\Anuja\\Downloads\\Direct_Payment - Sheet1.csv")

# Load the webpage
driver.get("https://dashboard.jodo.in/master-fee-data")
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/div/div/div[1]/div/div/input'))).send_keys('8638542842')
wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/div/div/div[2]/button'))).click()
time.sleep(20)
row=0
while row < len(df):
    driver.get(df['Link'][row])
    unpaid_amount = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div/div/div/div[2]/div[1]/div[3]/div/h6')))
    print(unpaid_amount.text)
    if unpaid_amount.text != '₹0.00':
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/button[3]'))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/div[2]/div[4]/div[1]/button'))).click()
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="paymentDetails_0_amount"]'))).clear()
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="paymentDetails_0_amount"]'))).send_keys(df['Direct Payment to be added'][row])
        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="paid_at"]'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="paid_at"]'))).send_keys('27-07-2023')
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="mode"]'))).click()
        wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div[6]'))).click()
        wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/form/div[4]/div[2]/div/div/input'))).send_keys('NA')
        wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/form/div[6]/div/div/div/div/button'))).click()
        print()
        row = row + 1

    else:
        row = row + 1
        continue
print(df)
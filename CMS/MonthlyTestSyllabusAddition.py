import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Initialize the WebDriver
service_obj = Service("C:\\Users\\Anuja\\Desktop\\python automation\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
wait = WebDriverWait(driver,40,ignored_exceptions=[Exception],poll_frequency=2)
action_chains = ActionChains(driver)
driver.maximize_window()

# Database
df = pd.read_csv("C:\\Users\\Anuja\\Downloads\\MT Syllabus - Sheet1 (1).csv")
df.replace(to_replace=np.NaN,value=' ',inplace=True)
# Login to CMS
# Load the webpage
driver.get("https://tutor-plus-cms-staging.tllms.com/neo_courses")
wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/a'))).click()
email = 'pratik.sondkar@byjus.com'
wait.until(EC.presence_of_element_located((By.ID, 'email'))).send_keys(email)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="signInForm"]/div[4]/button'))).click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="identifierId"]'))).send_keys(email)
wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="identifierNext"]/div/button/span'))).click()
password = 'Pratik@7682'
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input'))).send_keys(password)
wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="passwordNext"]/div/button/span'))).click()

#Clicking on Raw Topic
wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div/div/ul/div[10]/div[1]'))).click()
row = 0
while row < len(df):
    #Editing raw topic
    driver.get(f'https://tutor-plus-cms-staging.tllms.com/raw_topics/{int(df["RT ID"][row])}/edit')
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[2]/div[3]/div[1]/div[1]/div[5]/div[1]/div/div/span/img'))).click()

    click_count = 9
    for i in range(click_count):
        wait.until(EC.element_to_be_clickable((By.XPATH,'(//button[@type="button"])[7]'))).click()
    chapter_loc = wait.until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[4]/div[3]/div[2]/div/div[1]/div[2]/div/div/input')))
    j=1
    for i in chapter_loc:
        chapter = str(df.iloc[row, j])
        i.clear()
        i.send_keys(chapter)
        j += 1
    # Clicking on the save button
    wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div[3]/div[4]/button[2]'))).click()

    # Addition of Description
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div[1]/div[1]/div[7]/div/div/textarea'))).clear()
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[2]/div[3]/div[1]/div[1]/div[7]/div/div/textarea'))).send_keys(df['Description'][row])

    #Clicking on the save button
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[2]/div[3]/div[2]/button'))).click()
    print(f"Syllabus in RT ID - {int(df['RT ID'][row])} is added." )
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[2]/div[3]/div[1]/div[2]/button')))
    row = row + 1
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Initialize the WebDriver
service_obj = Service("C:\\Users\\Anuja\\Desktop\\python automation\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

# Database
df = pd.read_csv("C:\\Users\\Anuja\\Downloads\\MT Syllabus.csv").copy()

# Login to CMS
driver.switch_to.new_window('tab')
# Load the webpage
driver.get("https://tutor-plus-cms-staging.tllms.com/neo_courses")
driver.find_element(By.XPATH,'//*[@id="root"]/div/div/a').click()
time.sleep(1)
'''input("Enter your email ID: ")'''
email = "pratik.sondkar@byjus.com"
driver.find_element(By.ID, 'email').send_keys(email)
driver.find_element(By.XPATH, '//*[@id="signInForm"]/div[4]/button').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="identifierId"]').send_keys(email)
driver.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button/span').click()
time.sleep(5)
'''input("Enter your password: ")'''
password = "Pratik@7682"
driver.find_element(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
driver.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button/span').click()
time.sleep(12)

row = 0
while row < len(df):
    #Editing raw topic
    driver.get(f'https://tutor-plus-cms-staging.tllms.com/raw_topics/{df["RT ID"][row]}/edit')
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[3]/div[1]/div[1]/div[5]/div[2]/div/label/div').click()
    time.sleep(0.5)
    click_count = 9
    for i in range(click_count):
        driver.find_element(By.XPATH,'(//button[@type="button"])[7]').click()
        time.sleep(0.25)
    chapter_loc = driver.find_elements(By.XPATH,'/html/body/div[4]/div[3]/div[2]/div/div[1]/div[2]/div/div/input')
    j=1
    for i in chapter_loc:
        chapter = df.iloc[row, j]
        i.send_keys(chapter)
        j= j+1
    # Clicking on the save button
    driver.find_element(By.XPATH,'/html/body/div[4]/div[3]/div[4]/button[2]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[3]/div[1]/div[1]/div[7]/div/div/textarea').send_keys(df['Description'][row])

    #Clicking on the save button
    driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[3]/div[2]/button').click()
    print(f"Syllabus in RT ID - {df['RT ID'][row]} is added." )
    row = row + 1
    time.sleep(3)




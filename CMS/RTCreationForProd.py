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
df = pd.read_csv("C:\\Users\\Anuja\\Downloads\\RT Data.csv")

# Login to CMS
driver.switch_to.new_window('tab')
# Load the webpage
driver.get("https://tutor-plus-cms.tllms.com/neo_courses")
driver.find_element(By.XPATH,'//*[@id="root"]/div/div/a/span[1]').click()
email = input("email: ")
driver.find_element(By.ID, 'email').send_keys(email)
driver.find_element(By.XPATH, '//*[@id="signInForm"]/div[3]/button').click()
driver.find_element(By.XPATH,'//*[@id="identifierId"]').send_keys(email)
driver.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button/span').click()
time.sleep(5)
password = input("Enter your password: ")
driver.find_element(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
driver.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button/span').click()
time.sleep(8)

#Clicking on raw topic
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div/div/ul/div[10]/div').click()
time.sleep(10)
row = 0
while row < len(df):
    pass
    # Clicking on Create new Topic
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div/button').click()

    # clicking on class type
    driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[3]/div[1]/div[1]/div[1]/div/div/div/div/div').click()
    time.sleep(1)
    class_type = driver.find_elements(By.XPATH, '//*[@id="menu-"]/div[3]/ul//li')
    for i in class_type:
        if i.text == df['Class Type'][row]:
            i.click()
            break
    # Entering Topic Name:

    topic_name_locator = driver.find_element(By.CSS_SELECTOR,'input.input-box[placeholder="Enter topic name"]').send_keys(df['Topic Name'][row])

    # Entering Topic display name:

    topic_display_name_locator = driver.find_element(By.CSS_SELECTOR,'input.input-box[placeholder="Enter topic display name"]').send_keys(df['Topic Display Name'][row])

    # Selecting Subject:

    subject_click = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[3]/div[1]/div[1]/div[4]/div/div/div/div/div').click()
    subject = driver.find_elements(By.XPATH,'//*[@id="menu-"]/div[3]/ul//li')
    for li in subject:
        if li.text == df['Subject'][row]:
            li.click()
            break

    # Chapter Addition
    if df['Class Type'][row] == 'Regular Session':
        chap_loc = driver.find_element(By.CSS_SELECTOR,'input[placeholder="Enter Chapter"]').send_keys(df['Chapter Name'][row])
    elif df['Class Type'][row] == 'Monthly Test Session':
        pass

    #Grade Addition

    grade_txt_box_loc = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[3]/div[1]/div[1]/div[6]/div/div/div/div/div').click()
    grade = driver.find_elements(By.XPATH,'//*[@id="menu-"]/div[3]/ul//li')
    for li in grade:
        if li.text == df['Grade'][row]:
            li.click()

    # Saving the Raw Topic

    save_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div[2]/button').click()
    time.sleep(2)

    # Clicking on checkbox after saving Raw Topic

    checkbox_click = driver.find_element(By.CSS_SELECTOR,'input[name="selectAll"]').click()
    time.sleep(2)

    # Saving RT ID in Dataframe

    rt_id = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div/div/a').text
    df['RT ID'][row] = rt_id

    #Publishing the RT ID

    driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div/div[2]/button[1]').click()
    time.sleep(5)
    print(f'{row} - {df["MID"][row]} - {df["RT ID"][row]}')
    row = row + 1
    df.to_csv("C:\\Users\\Anuja\\Desktop\\CMS Automation\\output.csv")
print(df)

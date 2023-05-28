import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
service_obj = Service("C:\\Users\\Anuja\\Desktop\\python automation\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
wait = WebDriverWait(driver, 30, poll_frequency=2, ignored_exceptions=[Exception])
driver.maximize_window()

# Database
df = pd.read_csv("C:\\Users\\Anuja\\Downloads\\RT Data.csv").copy()

# Login to CMS
driver.switch_to.new_window('tab')
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

#Clicking on raw topic
wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div/div/ul/div[10]/div'))).click()
row = 0
while row < len(df):
    # Clicking on Create new Topic
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div/button'))).click()

    # clicking on class type
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[2]/div[3]/div[1]/div[1]/div[1]/div/div/div/div/div'))).click()
    class_type = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-"]/div[3]/ul//li'))).find_elements(By.XPATH,'//*[@id="menu-"]/div[3]/ul//li')
    for i in class_type:
        if i.text == df['Class Type'][row]:
            i.click()
            break
    # Entering Topic Name:

    topic_name_locator = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input.input-box[placeholder="Enter topic name"]'))).send_keys(df['Topic Name'][row])

    # Entering Topic display name:

    topic_display_name_locator = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input.input-box[placeholder="Enter topic display name"]'))).send_keys(df['Topic Display Name'][row])

    # Selecting Subject:

    subject_click = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[2]/div[3]/div[1]/div[1]/div[4]/div/div/div/div/div'))).click()
    subject = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="menu-"]/div[3]/ul//li')))
    for li in subject:
        if li.text == df['Subject'][row]:
            li.click()
            break

    # Chapter Addition
    if df['Class Type'][row] == 'Regular Session':
        chap_loc = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[placeholder="Enter Chapter"]'))).send_keys(df['Chapter Name'][row])
    elif df['Class Type'][row] == 'Monthly Test Session':
        pass

    #Grade Addition

    grade_txt_box_loc = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[2]/div[3]/div[1]/div[1]/div[6]/div/div/div/div/div'))).click()
    grade = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="menu-"]/div[3]/ul//li'))).find_elements(By.XPATH,'//*[@id="menu-"]/div[3]/ul//li')
    for li in grade:
        if li.text == df['Grade'][row]:
            li.click()

    # Saving the Raw Topic

    save_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div[2]/button'))).click()

    # Clicking on checkbox after saving Raw Topic

    checkbox_click = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[name="selectAll"]'))).click()

    # Saving RT ID in Dataframe

    rt_id = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div/div/a'))).text
    df['RT ID'][row] = rt_id

    #Publishing the RT ID

    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[2]/div/div[2]/div/div[2]/button[1]'))).click()
    alert = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="message-id"]')))
    print(f'{row} - {df["MID"][row]} - {df["RT ID"][row]}')
    row = row + 1
    df.to_csv("C:\\Users\\Anuja\\Desktop\\CMS Automation\\output.csv")
print(df)

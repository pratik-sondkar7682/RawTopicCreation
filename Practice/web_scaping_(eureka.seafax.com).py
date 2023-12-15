from tabulate import tabulate
from selenium import webdriver
from selenium.common import TimeoutException, ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import csv

# Initialize the WebDriver
service_obj = Service("C:\\Users\\Anuja\\Desktop\\Captain_Fresh\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[Exception])
driver.maximize_window()

# Load the webpage
driver.get("https://eureka.seafax.com/")

# Function for saving data in csv
def save_to_csv(data, file_path):
    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

#Login
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="uName"]'))).send_keys('487488')
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="password"]'))).send_keys('CapF@1234')
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginBTN"]'))).click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="new-search"]/a/span'))).click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="catmooptionchecklist_0"]'))).click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="view-results"]'))).click()
total_companies = len(wait.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="companiesGrid"]//tr'))))
i=1

while i<10:
    company = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[2]/div[3]/div[4]/div/table/tbody/tr['+str(i)+']/td[2]/a')))
    print(i,'Company Name:',company.text)

    #General Info
    print('General Info')
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div[3]/div[4]/div/table/tbody/tr['+str(i)+']/td[2]/a'))).click()
    time.sleep(3)
    GI = [['','',f'{company.text}','General Info']]
    total_rows = len(wait.until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[2]/div[2]/div[4]/div/div[2]/table/tbody[1]/tr'))))
    total_columns = len(wait.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="tabs1"]/tr[1]/td'))))
    row_gi = 1
    while row_gi<=total_rows:
        column_gi = 1
        data = []
        while column_gi <= total_columns:
            try:
                entry = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[4]/div/div[2]/table/tbody[1]/tr['+str(row_gi)+']/td['+str(column_gi)+']').text
                # print(entry)
                data.append(entry)
                column_gi = column_gi + 1
            except TimeoutException:
                column_gi = column_gi + 1
                continue
            except NoSuchElementException:
                column_gi = column_gi + 1
                continue
        GI.append(data)
        row_gi = row_gi + 1
    save_to_csv(GI, 'file1.csv')
    table = tabulate(GI,tablefmt="grid")
    print(table)


    #Business Details
    print('Business Details')
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="profile"]/div[2]/ul/li[2]/a'))).click()
    total_rows = len(wait.until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[2]/div[2]/div[4]/div/div[2]/table/tbody[2]/tr'))))
    total_columns = len(wait.until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[2]/div[2]/div[4]/div/div[2]/table/tbody[2]/tr[1]/td'))))
    BD = [['','',f'{company.text}','Business Details']]
    row_BD = 1
    while row_BD<=total_rows:
        column_BD = 1
        data = []
        while column_BD <= total_columns:
            entry = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[2]/div[4]/div/div[2]/table/tbody[2]/tr['+str(row_BD)+']/td['+str(column_BD)+']'))).text
            data.append(entry)
            column_BD = column_BD + 1
        BD.append(data)
        row_BD = row_BD+1
    save_to_csv(BD, 'file1.csv')
    table = tabulate(BD,tablefmt="grid")
    print(table)

    # Contacts
    print('Contacts')
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="profile"]/div[2]/ul/li[3]/a'))).click()
    total_rows = len(wait.until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[2]/div[2]/div[4]/div/div[2]/table/tbody[3]/tr'))))
    total_columns = len(wait.until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[2]/div[2]/div[4]/div/div[2]/table/tbody[3]/tr/td'))))
    CO = [['','',f'{company.text}','Contacts']]
    row_CO = 1
    while row_CO<=total_rows:
        column_CO = 1
        data = []
        while column_CO<=total_columns:
            entry = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[2]/div[4]/div/div[2]/table/tbody[3]/tr['+str(row_CO)+']/td['+str(column_CO)+']'))).text
            data.append(entry)
            column_CO = column_CO + 1
        CO.append(data)
        row_CO = row_CO+1
    save_to_csv(CO, 'file1.csv')
    table = tabulate(CO,tablefmt="grid")
    print(table)
    print('\n')
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="profile"]/img'))).click()
    time.sleep(2)
    i=i+1

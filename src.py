import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = '/usr/bin/chromedriver'
chrome_service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=chrome_service)

# open the chrome driver and wait for 20 seconds for the page to load
browser.get('https://hprera.nic.in/PublicDashboard')
time.sleep(20)

# xpath of the RERA numbers of first 5 projects
url1 = "/html/body/div[4]/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[1]/div[1]/div/div/div[1]/div/div/a"
url2 = "/html/body/div[4]/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div/a"
url3 = "/html/body/div[4]/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[1]/div[1]/div/div/div[3]/div/div/a"
url4 = "/html/body/div[4]/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[1]/div[1]/div/div/div[4]/div/div/a"
url5 = "/html/body/div[4]/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[1]/div[1]/div/div/div[5]/div/div/a"
urls = [url1, url2, url3, url4, url5]

print("The Details of the first 5 projects are as follows: \n")

# loop through the urls and extract the details of the projects
for url in urls:
    browser.find_element(By.XPATH,url).click()

    time.sleep(7)
    rows = browser.find_elements(By.TAG_NAME,'tr')

   # dictionary to store the details of the projects
    info_mapping = {
        'Name': None,
        'PAN No.': None,
        'GSTIN No.': None,
        'Permanent Address': None,
    }

    # filter the required fields from the table
    for row in rows:
        cells = row.find_elements(By.TAG_NAME,'td')
        if cells:
            cell_text = cells[0].text.strip()
            if cell_text in info_mapping:
                info_mapping[cell_text] = cells[1].text.strip()

    # Printing the extracted information
    for key, value in info_mapping.items():
        if key == 'Permanent Address' and value.endswith('Address Proof'):
            value = value.rsplit('Address Proof', 1)[0].strip()
        elif key == 'PAN No.' and value.endswith('PAN Card'):
            value = value.rsplit('PAN Card', 1)[0].strip()
        elif key == 'PAN No.' and value.endswith('PAN File'):
            value = value.rsplit('PAN File', 1)[0].strip()
        elif key == 'GSTIN No.' and value.endswith('GST Certificate'):
            value = value.rsplit('GST Certificate', 1)[0].strip()
        print(f"{key}: {value}")
    print()
    
    # Close the details page and go back to the main page
    browser.find_element(By.XPATH,"/html/body/div[4]/div/div/div/div[1]/div/div/div[2]/div/div/div[3]/button").click()
    


from pickle import STOP
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import time
import os, sys

option = Options()
option.add_experimental_option("detach", True)

base_url = 'http://demo.oshinit.com/'

def automateMortgageWebpage(principle: float = 0, interest: float = 0, period: float = 0) -> list:
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)
        driver.maximize_window()
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)
        time.sleep(4)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'a')))
        link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Mortgage')
        link.click()
        time.sleep(5)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(5)
        mortgage_amount = driver.execute_script("""return document.querySelector('os-tab').querySelector('article').querySelector('os-panel').querySelector('os-input[data-quantity-type="principle-loan"]').shadowRoot.querySelector('input')""")
        mortgage_amount.send_keys(principle)
        mortgage_amount.send_keys(Keys.ENTER)
        mortgage_period = driver.execute_script("""return document.querySelector('os-tab').querySelector('article').querySelector('os-panel').querySelector('os-input[data-quantity-type="loan-period"]').shadowRoot.querySelector('input')""")
        mortgage_period.send_keys(period)
        mortgage_period.send_keys(Keys.ENTER)
        mortgage_rate = driver.execute_script("""return document.querySelector('os-tab').querySelector('article').querySelector('os-panel').querySelector('os-input[data-quantity-type="interest-rate"]').shadowRoot.querySelector('input')""")
        mortgage_rate.send_keys(interest)
        mortgage_rate.send_keys(Keys.ENTER)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        webpage = bs(driver.page_source, 'lxml')

    except Exception as e: print(e)
    return webpage

def extractMortgageData(soup: list =[]):
    try:
        table_data = []
        for table in soup.select('.table table'):
            row = table.find_all('tr')

            header = row[0]
            headeTitles = []
            if '<th>' in str(header):
                headerRow = header.find_all('th')
                for headerCell in headerRow:
                    headeTitles.append(headerCell.get_text().strip())

            headerLength = len(headeTitles)
            if headerLength > 0:
                for cell in row[1:]:
                    row_data = []
                    if '<td>' in str(cell):
                        content = cell.find_all('td')
                        contentList = []
                        cell_data = {}
                        for i in range(headerLength):  
                            cell_data[headeTitles[i]] = content[i].get_text().strip()
                            contentList.append(cell_data)
                        row_data.append(contentList)
                    else:
                        row_data = []
                    table_data.append(row_data)
        return table_data
    except Exception as e: print(e)

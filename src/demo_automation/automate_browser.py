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

def autoWebpage():
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)
        driver.maximize_window()
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)
        time.sleep(4)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'a')))
        link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Mortgage')
        link.click()
        time.sleep(6)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        time.sleep(6)
        mortgage_amount = driver.execute_script("""return document.querySelector('os-tab').querySelector('article').querySelector('os-panel').querySelector('os-input[data-quantity-type="principle-loan"]').shadowRoot.querySelector('input')""")
        mortgage_amount.send_keys(350000)
        mortgage_amount.send_keys(Keys.ENTER)
        mortgage_period = driver.execute_script("""return document.querySelector('os-tab').querySelector('article').querySelector('os-panel').querySelector('os-input[data-quantity-type="loan-period"]').shadowRoot.querySelector('input')""")
        mortgage_period.send_keys(360)
        mortgage_period.send_keys(Keys.ENTER)
        mortgage_rate = driver.execute_script("""return document.querySelector('os-tab').querySelector('article').querySelector('os-panel').querySelector('os-input[data-quantity-type="interest-rate"]').shadowRoot.querySelector('input')""")
        mortgage_rate.send_keys(1.6)
        mortgage_rate.send_keys(Keys.ENTER)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(20)
        webpage = bs(driver.page_source, 'lxml')
        print(webpage)
    except Exception as e: print(e)

from pickle import STOP
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import time
import os, sys

base_url = 'http://demo.oshinit.com/'

def autoWebpage():
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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
    except Exception as e: print(e)

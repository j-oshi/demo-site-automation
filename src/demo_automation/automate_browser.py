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

# parent_dir = os.path.abspath('..')
# if parent_dir not in sys.path:
#     sys.path.append(parent_dir)

def autoWebpage():
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)
        time.sleep(4)
#     #     wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_class)))
#     #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     #     time.sleep(6)
#     #     result = bs(driver.page_source, 'lxml')
#     # except NoSuchElementException:
#     #     print("Error finding element")
#     # except ConnectionError:
#     #     print("No connection")
    except:
        print("Something else went wrong") 

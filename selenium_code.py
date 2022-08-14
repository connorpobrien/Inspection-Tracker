
import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# set location to the location of the webdriver
s = Service('/usr/local/bin/chromedriver')

driver = webdriver.Chrome(service=s)
driver.get("https://amazon.com/")
time.sleep(5)

driver.refresh()
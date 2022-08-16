# TODO: Use beautiful soup module
# TODO: Use pandas module

import time
import webbrowser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from bs4 import BeautifulSoup
import requests

# set location to the location of the webdriver
# XPATH -> //*[@id="cmbscheduledDate"]
s = Service('/usr/local/bin/chromedriver')


def refresh_page(page, seconds, xpath):
    """
    :param page: link to site -> str
    :param seconds: how often to reload page -> int
    :return: uses selenium to reload designated chrome page
    """
    driver = webdriver.Chrome(service=s)
    driver.get(page)

    # infinite loop to reload page and search for
    num_reloads = 1
    while num_reloads > 0:
        time.sleep(seconds)
        driver.refresh()
        driver.find_element(By.XPATH, xpath).click()


def get_html(page_url):
    """
    :param url: url of a website
    :return: html content on page
    """
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    return page.content


def inspection_available(page_html):
    """
    checks whether an inspection is available
    :param page_html: html contents of website
    :return: True is inspection is available
    """
    soup = BeautifulSoup(page_html, 'html.parser')
    inspection_status = soup.findAll

def notify(email):
    """
    :param email: email address of recipient
    :return: sends email to address if search_page is found to be true
    """
    pass


def main():
    print(get_html('https://sjpermits.org/permits/ir/detail_5.asp?PageUrl=../common/inspections.asp&peoplersn=682965&PageDescription=Return%20to%20list%20of%20permits&folderrsn=1979438'))


if __name__ == '__main__':
    main()
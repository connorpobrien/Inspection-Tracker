
import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# set location to the location of the webdriver
s = Service('/usr/local/bin/chromedriver')


def refresh_page(page, seconds):
    """
    :param page: link to site -> str
    :param seconds: how often to reload page -> int
    :return: uses selenium to reload designated chrome page
    """
    driver = webdriver.Chrome(service=s)
    driver.get(page)
    time.sleep(seconds)

    driver.refresh()


def main():
    webpage = input("Enter the url for the webpage: ")
    seconds = input("Enter how often you would like to reload the page: ")
    refresh_page(webpage, seconds)


if __name__ == '__main__'
    main()
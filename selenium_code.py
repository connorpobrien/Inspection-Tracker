# TODO: Use beautiful soup module
# TODO: Use pandas

import time
import webbrowser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# set location to the location of the webdriver
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

def search_page(xpath):
    """
    :param xpath: xpath to search for on a page
    :return: True if phrase is found, false if not
    """
    return webbrowser.find_element_by_xpath(xpath)


def notify(email):
    """
    :param email: email address of recipient
    :return: sends email to address if search_page is found to be true
    """
    pass


def main():
    # user input data
    webpage_url = input("Enter the url for the webpage: ")
    seconds = eval(input("Enter how often you would like to reload the page (seconds): "))
    content_xpath = input("Enter what you are searching for on the page: ")
    email = input("Enter your email: ")
    print("If '{0}' is found on '{1}', you will receive an email at '{2}'!".format(content_xpath, webpage_url, email))

    # run code
    refresh_page(webpage_url, seconds, content_xpath)


if __name__ == '__main__':
    main()
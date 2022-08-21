import time
import webbrowser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from bs4 import BeautifulSoup
import requests

# set location to the location of the webdriver
s = Service('/usr/local/bin/chromedriver')


def load_page_and_sign_in(page_url, login_1, login_2, driver):
    """
    Loads SJ building department website and signs in to inspection page
    :param page_url: url of website
    :param login_1: login phrase for 1st sign in page
    :param login_2: login phrase for 2nd sign in page
    :return: loads inspection webpage using selenium and logs in
    """
    # load website
    driver.get(page_url)

    # input login phrase for 1st page and click enter
    first_input = driver.find_element(By.ID, 'cin')
    first_input.send_keys(login_1)
    enter_button = driver.find_element(By.NAME, 'enter')
    enter_button.click()

    # click continue on second page
    continue_button = driver.find_element(By.XPATH, '//*[@id="container"]/table/tbody/tr/td/table/tbody/tr[2]/td/form/input[2]')
    continue_button.click()

    # confirm box on third page and click submit
    confirm_box = driver.find_element(By.ID, 'Confirmation')
    confirm_box.click()
    submit_button = driver.find_element(By.NAME, 'B1')
    submit_button.click()

    # input login phrase for 2nd page and click 'search'
    permit_box = driver.find_element(By.NAME, 'permitnum')
    permit_box.send_keys(login_2)
    search_button = driver.find_element(By.XPATH, '//*[@id="container"]/table/tbody/tr/td/form/font/font/table/tbody/tr[3]/td/p/input')
    search_button.click()


def refresh_page(seconds, driver):
    """
    :param driver: driver from 'load_page' function
    :param seconds: how often to reload page -> int
    :return: uses selenium to reload designated chrome page
    """

    time.sleep(seconds)
    driver.refresh()


def get_html(page_url):
    """
    :param page_url: url of a website
    :return: html content on page
    """
    pass
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(page_url, headers=headers)
    return page.content


def inspection_available(driver, month_date, day_date):
    """
    :param driver:
    :param month_date:
    :param day_date:
    :return:
    """
    page_source = requests.get(driver.current_url)
    soup = BeautifulSoup(page_source.content, "html.parser")

    print(soup)

    content = soup.find_all('td', class_='menu')

    print(content)

    # dates = []
    # date_selector = soup.find_all('span', select_='cmbscheduledDate')
    #
    # for i in date_selector:
    #     dates.append(i)
    #
    # return dates



def play_duration():
    """
    Plays sound from computer speakers
    """
    pass


def main():

    # get all necessary info from user input
    url = 'https://sjpermits.org/permits/general/scheduleinspection.asp'
    username = input("Enter the permit number: ")
    password = "2022" + username
    permit_month = input("Enter the month of the permit that you are waiting for: ")
    permit_day = input("Enter the day of the permit that you are waiting for: ")

    # define driver (global)
    global_driver = webdriver.Chrome(service=s)

    # load webpage and get to inspection page
    load_page_and_sign_in(url, username, password, global_driver)

    time.sleep(2)

    inspection_available(global_driver, permit_month, permit_day)


if __name__ == '__main__':
    main()

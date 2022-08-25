import time
import webbrowser
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from bs4 import BeautifulSoup

from pygame import mixer

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


def inspection_available(driver, inspection_date, type_of_inspection):
    """
    :param driver:
    :param inspection_date:
    :param type_of_inspection:
    :return:
    """

    # retrieve html of whole page
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # format inspection type variable (str)
    inspection_type = "MyForm" + type_of_inspection[0].upper()

    # narrow down html
    content = soup.find_all('form', attrs={'name': inspection_type})

    # convert content to string to easily parse
    string_content = str(content)

    # return True if date is available
    if inspection_date in string_content:
        return True
    return False


def play_alert():
    """
    Plays sound from computer speakers
    """
    mixer.init()
    sound = mixer.Sound("mixkit-classic-alarm-995.wav")
    sound.play()


def main():
    # define driver (global)
    global_driver = webdriver.Chrome(service=s)

    # load webpage and get to inspection page
    load_page_and_sign_in(url, username, password, global_driver)

    # continue search until inspection is available, alert when found
    continue_searching = True
    repetitions = 0
    while continue_searching:
        if inspection_available(global_driver, inspection_date, type_of_inspection):
            play_alert()
            print("Inspection found on date inputted!")
            play_alert()
            time.sleep(10)
            continue_searching = False
        else:
            repetitions += 1
            print("Still searching!", "Number of times searched:", repetitions)
            print("-----------------")
            refresh_page(2, global_driver)


if __name__ == '__main__':
    print('~~~~~~~~~~~~~~~~~~~~~~~')
    # get all necessary info from user input
    url = 'https://sjpermits.org/permits/general/scheduleinspection.asp'
    username = input("Enter the permit number: ")
    password = "2022" + username
    print('-----------------------')
    type_of_inspection = input("Enter the type of inspection that you are looking for (Building, Electrical, "
                               "Plumbing/Mechanical, Fire, Hazmat): ")
    print('-----------------------')
    inspection_date = input("Enter the date of the permit that you are waiting for (Ex: 09/10/2022): ")
    print('-----------------------')
    print("Alarm will sound if inspection is available.")
    print('-----------------------')

    # run search
    main()

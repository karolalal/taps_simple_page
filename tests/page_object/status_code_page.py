from tests.helpers.support_functions import *
import requests
from time import sleep

status_code_tab = 'statuscodes-header'
status_code_content = 'statuscodes-content'
status_code_200 = '200siteAnchor'
status_code_305 = '305siteAnchor'
status_code_404 = '404siteAnchor'
status_code_500 = '500siteAnchor'


def click_status_code_tab(driver_instance):
    driver_instance.find_element(By.ID, status_code_tab).click()


def status_code_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, status_code_content)
    return elem.is_displayed()


def code_200_click(driver_instance):
    wait_for_visibility_of_element(driver_instance, status_code_200)
    driver_instance.find_element(By.ID, status_code_200).click()
    get_url = driver_instance.current_url
    req = requests.get(get_url)
    status_code = req.status_code
    try:
        if status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.ConnectionError:
        print('Connection error')
        return False


def code_305_click(driver_instance):
    wait_for_visibility_of_element(driver_instance, status_code_305)
    driver_instance.find_element(By.ID, status_code_305).click()
    get_url = driver_instance.current_url
    req = requests.get(get_url)
    status_code = req.status_code
    try:
        if status_code == 305:
            return True
        else:
            return False
    except requests.exceptions.ConnectionError:
        print('Connection error')
        return False


def code_404_click(driver_instance):
    wait_for_visibility_of_element(driver_instance, status_code_404)
    driver_instance.find_element(By.ID, status_code_404).click()
    get_url = driver_instance.current_url
    req = requests.get(get_url)
    status_code = req.status_code
    try:
        if status_code == 404:
            return True
        else:
            return False
    except requests.exceptions.ConnectionError:
        print('Connection error')
        return False


def code_500_click(driver_instance):
    wait_for_visibility_of_element(driver_instance, status_code_500)
    driver_instance.find_element(By.ID, status_code_500).click()
    get_url = driver_instance.current_url
    req = requests.get(get_url)
    status_code = req.status_code
    try:
        if status_code == 500:
            return True
        else:
            return False
    except requests.exceptions.ConnectionError:
        print('Connection error')
        return False







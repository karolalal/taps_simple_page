from tests.helpers.support_functions import *
from time import sleep

auth_header = 'basicauth-header'
auth_content = 'basicauth-content'
username = 'ba_username'
password = 'ba_password'
login_button = '//*[@id="content"]/button'
message = 'loginFormMessage'


def click_auth_tab(driver_instance):
    elem = driver_instance.find_element(By.ID, auth_header).click()


def auth_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, auth_content)
    return elem.is_displayed()


def send_correct_data(driver_instance):
    wait_for_visibility_of_element(driver_instance, username)
    name = driver_instance.find_element(By.ID, username)
    name.send_keys('admin')
    wait_for_visibility_of_element(driver_instance, password)
    passw = driver_instance.find_element(By.ID, password)
    passw.send_keys('admin')
    value = 'admin'
    if value == name.get_attribute("value") and value == passw.get_attribute("value"):
        log = driver_instance.find_element(By.XPATH, login_button).click()
        return True
    else:
        return False


def send_incorrect_data(driver_instance):
    wait_for_visibility_of_element(driver_instance, username)
    name = driver_instance.find_element(By.ID, username)
    name.send_keys('admin')
    wait_for_visibility_of_element(driver_instance, password)
    passw = driver_instance.find_element(By.ID, password)
    passw.send_keys('haslo')
    value = 'admin'
    if value != name.get_attribute("value") or value != passw.get_attribute("value"):
        return True
    else:
        return False


def message_visible(driver_instance):
    log = driver_instance.find_element(By.XPATH, login_button).click()
    wait_for_visibility_of_element(driver_instance, message)
    err_message = driver_instance.find_element(By.ID, message)
    if err_message.is_displayed():
        return True
    else:
        return False




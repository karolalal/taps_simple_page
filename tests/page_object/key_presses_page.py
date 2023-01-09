from selenium.webdriver import Keys
from tests.helpers.support_functions import *

key_presses_tab = 'keypresses-header'
key_press_content = 'keypresses-content'
input_field = 'target'
result = 'keyPressResult'


def click_key_presses_tab(driver_instance):
    driver_instance.find_element(By.ID, key_presses_tab).click()


def key_presses_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, key_press_content)
    return elem.is_displayed()


def key_presses_input(driver_instance):
    wait_for_visibility_of_element(driver_instance, input_field)
    elem = driver_instance.find_element(By.ID, input_field)
    elem.send_keys(Keys.TAB)
    text = 'You entered: TAB'
    message = driver_instance.find_element(By.ID, result).text
    if message == text:
        return True
    else:
        return False



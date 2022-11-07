from tests.helpers.support_functions import *
from time import sleep

error_info = 'container'
logged_in_message = 'loggedInMessage'
return_button = 'retrun button'


def error_info_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, error_info)
    return elem.is_displayed()


def logged_in_message_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, logged_in_message)
    return elem.is_displayed()


def return_main_page(driver_instance):
    wait_for_invisibility_of_element(driver_instance, return_button)
    elem = driver_instance.find_element(By.ID, return_button).click()


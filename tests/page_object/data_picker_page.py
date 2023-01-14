from tests.helpers.support_functions import *
from time import sleep

date_picker_tab = 'datepicker-header'
date_picker_content = 'datepicker-content'
date_picker_calendar = 'start'


def click_date_picker_tab(driver_instance):
    elem = driver_instance.find_element(By.ID, date_picker_tab).click()


def date_picker_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, date_picker_content)
    return elem.is_displayed()


def send_correct_keys_to_input(driver_instance):
    wait_for_visibility_of_element(driver_instance, date_picker_calendar, time_to_wait=1)
    elem = driver_instance.find_element(By.ID, date_picker_calendar)
    elem.send_keys('2110')
    value = '2020-10-21'
    if value == elem.get_attribute('value'):
        return True
    else:
        return False


def send_incorrect_keys_to_input(driver_instance):
    wait_for_visibility_of_element(driver_instance, date_picker_calendar, time_to_wait=1)
    elem = driver_instance.find_element(By.ID, date_picker_calendar)
    elem.send_keys('abc')
    value = 'abc'
    if value == elem.get_attribute('value'):
        return False
    else:
        return True


def send_outofscope_keys_to_input(driver_instance):
    wait_for_visibility_of_element(driver_instance, date_picker_calendar, time_to_wait=1)
    elem = driver_instance.find_element(By.ID, date_picker_calendar)
    elem.send_keys('20102021')
    value = '2021-10-20'
    if value == elem.get_attribute("value"):
        return False
    else:
        return True



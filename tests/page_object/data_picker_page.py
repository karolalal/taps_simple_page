from tests.helpers.support_functions import *

date_picker_tab = 'datepicker-header'
date_picker_content = 'datepicker-content'
date_picker_calendar = '//*[@id="start"]'


def click_date_picker_tab(driver_instance):
    elem = driver_instance.find_element(By.ID, date_picker_tab).click()


def date_picker_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, date_picker_content)
    return elem.is_displayed()


def send_correct_keys_to_input(driver_instance):
    wait_for_visibility_of_element_xpatch(driver_instance, date_picker_calendar)
    elem = driver_instance.find_element(By.XPATH, date_picker_calendar)
    elem.send_keys('21.08.2020')
    value = '2020-12-21'
    if value == elem.get_attribute('value'):
        return True
    else:
        return False


def send_incorrect_keys_to_input(driver_instance):
    wait_for_visibility_of_element_xpatch(driver_instance, date_picker_calendar)
    elem = driver_instance.find_element(By.XPATH, date_picker_calendar)
    elem.send_keys('15.38.988')
    value = '2020-15-38'
    if value == elem.get_attribute('value'):
        return False
    else:
        return True


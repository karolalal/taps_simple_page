from tests.helpers.support_functions import *
from time import sleep

form_header = 'form-header'
form_content = 'form-content'
f_name = 'fname'
l_name = 'lname'
submit_button = 'formSubmitButton'


def click_form_tab(driver_instance):
    driver_instance.find_element(By.ID, form_header).click()


def form_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, form_content)
    return elem.is_displayed()


def send_correct_data(driver_instance):
    first_name = driver_instance.find_element(By.ID, f_name)
    first_name.send_keys('Fabryka')
    last_name = driver_instance.find_element(By.ID, l_name)
    last_name.send_keys('Testow')
    value = 'Fabryka'
    value1 = 'Testow'
    if value == first_name.get_attribute("value") and value1 == last_name.get_attribute("value"):
        return True
    else:
        return False


def accept_alert(driver_instance):
    driver_instance.find_element(By.ID, submit_button).click()
    wait_for_visibility_of_alert(driver_instance)
    driver_instance.switch_to.alert.accept()


def send_incorrect_data(driver_instance):
    wait_for_visibility_of_element_message(driver_instance, l_name)
    last_name = driver_instance.find_element(By.ID, l_name)
    last_name.send_keys('Kowalski')
    driver_instance.find_element(By.ID, submit_button).click()
    first_name = driver_instance.find_element(By.ID, f_name)
    text = 'Wypełnij to pole.'
    wait_for_visibility_of_element_message(driver_instance, f_name)
    message = first_name.get_attribute("validationMessage")
    if text == message:
        return True
    else:
        return False



    # text = first_name.get_attribute("value")
    # #first_name.send_keys('')
    # # last_name = driver_instance.find_element(By.ID, l_name)
    # # last_name.send_keys('Kowalski')
    # #message = first_name.get_attribute('message')
    # message = 'Please fill out this field.'
    # if message == text:
    #     return True
    # else:
    #     return False
    #








from tests.helpers.support_functions import *

iFrame_tab = 'iframe-header'
iFrame_content = 'iframe-content'
button1 = 'simpleButton1'
button2 = 'simpleButton2'
iframe_main = 'iframe'
message = 'whichButtonIsClickedMessage'


def click_iframe_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, iFrame_tab)
    driver_instance.find_element(By.ID, iFrame_tab).click()


def hover_content_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, iFrame_content)
    return elem.is_displayed()


def click_button1_inside_iframe(driver_instance):
    wait_for_visibility_of_element(driver_instance, iframe_main)
    driver_instance.switch_to.frame(driver_instance.find_element(By.TAG_NAME, 'iframe'))
    driver_instance.find_element(By.ID, button1).click()
    mess = driver_instance.find_element(By.ID, message).text
    if mess == 'Button 1 was clicked!':
        return True
    else:
        return False


def click_button2_inside_iframe(driver_instance):
    wait_for_visibility_of_element(driver_instance, iframe_main)
    driver_instance.switch_to.frame(driver_instance.find_element(By.TAG_NAME, 'iframe'))
    driver_instance.find_element(By.ID, button2).click()
    mess = driver_instance.find_element(By.ID, message).text
    if mess == 'Button 2 was clicked!':
        return True
    else:
        return False
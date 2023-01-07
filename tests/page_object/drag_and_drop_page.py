from tests.helpers.support_functions import *
from time import sleep

drag_tab = 'draganddrop-header'
drag_content = 'draganddrop-content'
column_a = 'column-a'
column_b = 'column-b'


def click_drag_tab(driver_instance):
    driver_instance.find_element(By.ID, drag_tab).click()


def drag_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, drag_content)
    return elem.is_displayed()


def drag_and_drop_a_to_b(driver_instance):
    box_a = driver_instance.find_element(By.ID, column_a)
    box_b = driver_instance.find_element(By.ID, column_b)
    ActionChains(driver_instance).drag_and_drop(box_a, box_b).perform()
    # if box_a.location == box_b.location:
    #     return True
    # else:
    #     return False
    #ActionChains(driver_instance).click_and_hold(box_a).pause(2).move_to_element(box_b).perform()

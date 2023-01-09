import os.path
from tests.helpers.support_functions import *

drag_tab = 'draganddrop-header'
drag_content = 'draganddrop-content'
column_a = 'column-a'
column_b = 'column-b'
column_a_text = '//*[@id="column-a"]/header'
column_b_text = '//*[@id="column-b"]/header'


def click_drag_tab(driver_instance):
    driver_instance.find_element(By.ID, drag_tab).click()


def drag_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, drag_content)
    return elem.is_displayed()


def check_drag_and_drop(driver_instance):
    driver_instance.implicitly_wait(10)
    driver_instance.get('http://simpletestsite.fabrykatestow.pl/')

    with open(os.path.abspath('drag_and_drop_helper.js'), 'r') as js_file:
        line = js_file.readline()
        script = ''
        while line:
            script += line
            line = js_file.readline()

    driver_instance.execute_script(script + "jQuery('#column-a').simulateDragDrop({ dropTarget: '#column-b'});")
    return True

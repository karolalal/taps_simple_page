from tests.helpers.support_functions import *

hovers_tab = 'hovers-header'
hovers_content = 'hovers-content'
gentlemans_picture = '//*[@id="hovers-content"]/div/div[1]/img'
gentleman_link = '//*[@id="hovers-content"]/div/div[1]/div/a'

def click_hovers_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, hovers_content)
    elem = driver_instance.find_element(By.ID, hovers_tab)
    elem.click()

def hover_content_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, hovers_content)
    return elem.is_displayed()

def hover_over_element_and_clicked(driver_instance):
    hover_over_element(driver_instance, gentlemans_picture)
    elem = driver_instance.find_element(By.XPATH, gentleman_link)
    elem.click()

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.alert import Alert


def hover_over_element(driver_instance, xpath):
    elem = driver_instance.find_element(By.XPATH, xpath)
    hover = ActionChains(driver_instance).move_to_element(elem)
    hover.perform()


def wait_for_visibility_of_element(driver_instance, id, time_to_wait=10):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.ID, id)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_invisibility_of_element(inv_driver_instance, id, time_to_wait=8):
    inv_elem = WebDriverWait(inv_driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.ID, id)))
    return inv_elem


def wait_for_visibility_of_element_xpatch(driver_instance, xpatch, time_to_wait=10):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.XPATH, xpatch)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_visibility_of_alert(driver_instance):
    try:
        alert = WebDriverWait(driver_instance, 10).until(EC.alert_is_present())
    except TimeoutException:
        alert = False
    return alert


def wait_for_visibility_of_element_message(driver_instance, id):
    wait = WebDriverWait(driver_instance, 20)
    try:
        elem = wait.until(EC.visibility_of_element_located((By.ID, id))).get_attribute('validationMessage')
    except TimeoutException:
        elem = False
    return elem


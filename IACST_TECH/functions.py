"""
    Collection of all the functions necessary for this project is here. 
"""
#complete the functions denoted by pass
from selenium import webdriver
from selenium.webdriver.common.by import By
import constants
def login(rollnum : int, dob : int, driver : webdriver.Chrome):
    """
        Given a roll number, dob in string format and a driver. This function logins in the driver.
    """
    driver.get(constants.LOGIN_URL)
    iframe = driver.find_element(By.XPATH, constants.X_PATHS["pop_up_iframe"])
    driver.switch_to.frame(iframe) 
    driver.find_element(By.XPATH, constants.X_PATHS["close_pop_up"]).click()
    driver.switch_to.default_content()
    driver.find_element(By.XPATH, constants.X_PATHS["roll_num"]).send_keys(rollnum)
    driver.find_element(By.XPATH, constants.X_PATHS["dob"]).send_keys(dob)
    driver.find_element(By.XPATH, constants.X_PATHS["login"]).click()

def register(phonenum : int, driver):
    pass

def solve(rollnum : int, dob : int, percentage_required : float, driver):
    pass

def get_unsolved_set(rollnum : int, dob : int, driver):
    pass

def get_set_solved():
    pass
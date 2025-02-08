from selenium import webdriver
from selenium.webdriver.common.by import By
import constants
import pyautogui as pg
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from io import BytesIO
import os

def click_element(driver, path):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, path))
    )
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path)))
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)


def login(rollnum, date, driver):
    driver.get(constants.LOGIN_LINK)
    time.sleep(5)
    # click_element(driver, constants.DENY_ONTIFICATION)
    roll_input = driver.find_element(By.XPATH, constants.ROLL_NUM_INPUT)
    roll_input.clear()
    roll_input.send_keys(rollnum)

    time.sleep(5)
    dob_input = driver.find_element(By.XPATH, constants.DOB_INPUT)
    dob_input.clear()
    dob_input.send_keys(date) 
    pg.press('enter')
    time.sleep(10)
    createFolder(driver, "class_name", "11th","M06")
    time.sleep(2)
    takeScreenShot(driver, "class_name", "11th","M06")


def download_result(rollnum, date, driver, path):
    login(rollnum, date, driver)
    time.sleep(5)
    original_handle = driver.current_window_handle
    click_element(driver, constants.VIEW_RESULT)
    time.sleep(5)
    for handle in driver.window_handles:
        if handle != original_handle:
            driver.switch_to.window(handle)
            break
    click_element(driver, constants.PRINT)
    time.sleep(5)
    for i in range(constants.NUM_OF_TABS_AFTER_PRINT):
        pg.press('tab')
    pg.typewrite(path)
    pg.press('enter')
    
def createFolder(driver, pathLocation, set_class, set_name):
    folder_path = os.path.join(pathLocation, set_class, set_name)
    os.makedirs(folder_path, exist_ok=True) 
    print(f"Folder '{folder_path}' created successfully!")
    
def takeScreenShot(driver, pathLocation, set_class, set_name):
    screenshot = driver.get_screenshot_as_png()
    image = Image.open(BytesIO(screenshot))
    image.save(f"./{pathLocation}/{set_class}/{set_name}/screenshot.png")
    click_element(driver, constants.LOGIN_BUTTON)


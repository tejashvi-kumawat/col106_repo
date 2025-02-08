import functions
import time
from selenium import webdriver
def fxn():
    driver = webdriver.Chrome()
    functions.login("231920550069","01012008",driver)
    # functions.login("269520550070", "01012007",driver)
    # functions.download_result("231920550069","01012008",driver, "name")
    functions.time.sleep(1000) 

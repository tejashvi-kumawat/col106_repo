from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import functions
import constants
import time
options = Options()
# options.add_argument("--headless")  # Run Chrome in headless mode
# options.add_argument("--disable-gpu")  # Disable GPU acceleration (sometimes needed)
# options.add_argument("--window-size=1920x1080")  # Set a window size
rollnum = "231920550069"
dob = "01012008"
driver = webdriver.Chrome(options=options)

functions.login(rollnum= rollnum, dob= dob, driver= driver)
print(driver.title)  # Print page title
time.sleep(550)
driver.quit()
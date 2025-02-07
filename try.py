from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set Chrome options to run headless
chrome_options = Options()
chrome_options.add_argument("--headless")

# Initialize the Chrome driver with options
driver = webdriver.Chrome(options=chrome_options)
# Navigate to the desired URL
driver.get("https://google.com")
# Print the page title
print("Page Title:", driver.title)
# Clean up and close the browser
driver.quit()

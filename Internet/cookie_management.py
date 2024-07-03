from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up browser options
chrome_options = Options()
chrome_options.add_argument("--headless")  

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://www.google.com/")

    # Set a cookie value
    driver.add_cookie({'name': 'myCookie', 'value': '123'})

    # Get a cookie value
    cookie = driver.get_cookie('myCookie')
    print(f"Cookie: {cookie}")

    # Remove a cookie value
    driver.delete_cookie('myCookie')

    # Check that the value is deleted
    cookie = driver.get_cookie('myCookie')
    print(f"Cookie after removal: {cookie}")

finally:
    driver.quit()
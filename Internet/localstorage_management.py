from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up browser options
chrome_options = Options()
chrome_options.add_argument("--headless") 

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://www.google.com/")

    # Set a localStorage value
    driver.execute_script("localStorage.setItem('myKey', '123');")

    # Get a localStorage value
    value = driver.execute_script("return localStorage.getItem('myKey');")
    print(f"Value from LocalStorage: {value}")

    # Remove a localStorage value
    driver.execute_script("localStorage.removeItem('myKey');")

    # Check that the value is deleted
    value = driver.execute_script("return localStorage.getItem('myKey');")
    print(f"Value after removal: {value}")

finally:
    driver.quit()
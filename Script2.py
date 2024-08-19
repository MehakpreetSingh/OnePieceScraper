import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twocaptcha import TwoCaptcha
# Set up the Chrome WebDriver
edge_driver_path = r'C:\Users\mehak\Downloads\msedgedriver.exe'

# Set up Edge options
edge_options = webdriver.EdgeOptions()

# Set up the Edge service
service = Service(edge_driver_path)

# Initialize the WebDriver
driver = webdriver.Edge(service=service, options=edge_options)

# Open the target webpage
driver.get("https://susflix.tv/")  # Replace with the actual URL

# Click the login button
login_button = driver.find_element(By.XPATH, "//a[@href='/login']/button")
login_button.click()

# Wait for the login page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'phone_number')))

# Input the login credentials
username_input = driver.find_element(By.NAME, 'phone_number')
password_input = driver.find_element(By.NAME, 'password')

username_input.send_keys("huhululu765")  # Replace with your actual phone number
password_input.send_keys("Wy.2mm84riGt#9$")  # Replace with your actual password

# # Wait for the reCAPTCHA to be manually solved
# site_key = driver.find_element(By.CLASS_NAME, 'g-recaptcha').get_attribute('data-sitekey')
# current_url = driver.current_url

# # 2Captcha API request
# api_key = 'c9b353f348abd9dd44bfc4dc8d7e3d6e'  # Replace with your actual 2Captcha API key
# print("Solving Captcha")
# solver = TwoCaptcha(api_key)
# response = solver.recaptcha(sitekey=site_key, url=current_url)
# code = response['code']
# print(f"Successfully solved the Captcha. The solve code is {code}")

# Wait for the user to solve the reCAPTCHA manually
print("Please solve the reCAPTCHA manually.")
WebDriverWait(driver, 30000).until(EC.presence_of_element_located((By.ID, 'g-recaptcha-response')))


# Click the "Sign In" button
sign_in_button = driver.find_element(By.CSS_SELECTOR, "input.login-submit")
sign_in_button.click()

# Wait for the login to complete and the next page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
print("Login completed. The browser will remain open for further actions.")
input("Press Enter to close the browser...")
# Add any further actions here, if needed

# Close the browser
# driver.quit()

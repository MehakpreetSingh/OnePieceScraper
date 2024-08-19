# prompt: i have a website https://ee3.me/ which i want to scrape using selenium where the first page is login page with same url and then the login form is hidden but the url remains same  but i changes to movies displayed 

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
import time

# Path to your Edge WebDriver executable
edge_driver_path = r'C:\Users\mehak\Downloads\msedgedriver.exe'

# Set up Edge options
edge_options = webdriver.EdgeOptions()

# Set up the Edge service
service = Service(edge_driver_path)

# Initialize the WebDriver
driver = webdriver.Edge(service=service, options=edge_options)

# Login to the website
driver.get("https://ee3.me/")


form_id = "login_form" 
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, form_id))
)

# Locate the form by ID
form_element = driver.find_element(By.ID, form_id)

# Locate the button with class name 'red' inside the form
button_class_name = "red"  # Replace with the actual class name of the button
button_element = form_element.find_element(By.CLASS_NAME, button_class_name)

# Find the username and password fields
username_field = form_element.find_element(By.NAME, "user")
password_field = form_element.find_element(By.NAME, "pass")

# Enter the username and password
username_field.send_keys("mehakbrar811")
password_field.send_keys("npG9vZtYgZzp!v7")

# Click the button
button_element.click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "movies"))
)

# Initialize an empty list to store the movie data
movie_data = []

# Loop through the pages of movies
while True:
  # Get the page source
  html = driver.page_source

  # Parse the HTML with BeautifulSoup
  soup = BeautifulSoup(html, "html.parser")

  # Find all the movie elements
  movie_elements = soup.find_all("div", class_="movies")

  # Extract the movie data from each element
  for movie_element in movie_elements:
    # title = movie_element.find("p").text
    # year = movie_element.find("span", class_="year").text
    # rating = movie_element.find("span", class_="rating").text
    movie_data.append({"title": "title"})

  # Check if there is a next page
  # next_page_button = driver.find_element_by_class_name("next-page")
  # if next_page_button.get_attribute("href") is None:
  #   break

  # Click on the next page button
  # next_page_button.click()

# Convert the movie data to a pandas DataFrame
df = pd.DataFrame(movie_data)

# Print the DataFrame
print(df)

# Close the web driver
driver.quit()

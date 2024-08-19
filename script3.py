import json
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

# Replace this with the path to your Edge WebDriver
edge_driver_path = r'C:\Users\mehak\Downloads\msedgedriver.exe'
service = Service(edge_driver_path)
driver = webdriver.Edge(service=service)

# URL and range of IDs
base_url = "https://tokyoinsider.com/anime/O/One_piece_(TV)/episode/{id}"
start_id = 751
end_id = 752

# Iterate through the specified range of episode IDs
for episode_id in range(start_id, end_id + 1):
    url = base_url.format(id=episode_id)
    driver.get(url)
    time.sleep(2)  # Wait for the page to load

    # Find the <div id="inner_page">
    inner_page = driver.find_element(By.ID, "inner_page")

    # Extract the links and related information
    download_links = []
    containers = inner_page.find_elements(By.CSS_SELECTOR, "div.c_h2, div.c_h2b")

    for container in containers:
        # Get all <a> tags within the container
        link_tags = container.find_elements(By.TAG_NAME, "a")
        
        if len(link_tags) >= 2:  # Ensure there are at least two <a> tags
            second_link_tag = link_tags[1]  # Select the second <a> tag
            link_url = second_link_tag.get_attribute("href")
            link_text = second_link_tag.text.strip()

            # Extract additional info such as size, downloads, uploader, etc.
            finfo = container.find_element(By.CSS_SELECTOR, "div.finfo").text.strip()

            download_links.append({
                "link_text": link_text,
                "link_url": link_url,
                "info": finfo
            })

    # Save the extracted data to a JSON file
    json_filename = f"episode_{episode_id}.json"
    with open(json_filename, "w") as json_file:
        json.dump(download_links, json_file, indent=4)

    print(f"Saved data for episode {episode_id} to {json_filename}")

# Close the WebDriver
driver.quit()

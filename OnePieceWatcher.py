import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import streamlit as st

# Define the base URL and the range of episode IDs
base_url = "https://tokyoinsider.com/anime/O/One_piece_(TV)/episode/"
start_id = 751
end_id = 752

# Dictionary to hold the episode links
episode_links = {}

for episode_id in range(start_id, end_id + 1):
    # Construct the URL for the current episode
    url = f"{base_url}{episode_id}"

    # Fetch the page content
    response = requests.get(url)
    if response.status_code != 200:
        st.error(f"Failed to fetch {url}")
        continue

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the div with id 'inner_page'
    inner_page_div = soup.find('div', id='inner_page')
    if not inner_page_div:
        st.error(f"No inner_page div found for {url}")
        continue

    # Find all divs with class 'c_h2b' and 'c_h2'
    video_divs = inner_page_div.find_all('div', class_=['c_h2b', 'c_h2'])

    # Extract the href attribute from the second <a> tag
    for video_div in video_divs:
        a_tags = video_div.find_all('a', href=True)
        if len(a_tags) > 1:  # Check if there are at least two <a> tags
            second_a_tag = a_tags[1]  # Get the second <a> tag
            if '[HorribleSubs]' in second_a_tag.text:
                link = second_a_tag['href']
                # Add the link to the dictionary under the current episode ID
                episode_links[f"Episode {episode_id}"] = link
                break  # Stop searching once we've found the desired link

# Convert the dictionary to a DataFrame
df = pd.DataFrame(episode_links.items(), columns=['Episode', 'Link'])

# Construct the IINA URL scheme (if needed)
df['IINA Link'] = df['Link'].apply(lambda link: f'{link}')
df.drop(columns=['Link'], inplace=True)  # Drop the original 'Link' column

# Streamlit app
st.title("One Piece Video Player")

# Dropdown for episode selection
selected_episode = st.selectbox("Select an Episode", df['Episode'])

# Display the video player based on the selected episode
if selected_episode:
    link = df[df['Episode'] == selected_episode]['IINA Link'].values[0]
    st.video(link)

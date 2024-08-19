import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the base URL for episode links
base_url = "https://tokyoinsider.com/anime/O/One_piece_(TV)/episode/"

def fetch_episode(episode_id):
    url = f"{base_url}{episode_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    inner_page_div = soup.find('div', id='inner_page')
    if not inner_page_div:
        return None

    video_divs = inner_page_div.find_all('div', class_=['c_h2b', 'c_h2'])
    for video_div in video_divs:
        a_tags = video_div.find_all('a', href=True)
        if len(a_tags) > 1:
            second_a_tag = a_tags[1]
            if '[HorribleSubs]' in second_a_tag.text:
                video_link = second_a_tag['href']
                return video_link

    return None

def main():
    st.title("One Piece Episode Viewer")

    # Episode number input and search button
    episode_number = st.text_input("Enter Episode Number (e.g., 751)")

    if st.button('Search'):
        if not episode_number.isdigit():
            st.error("Please enter a valid episode number.")
            return

        episode_id = int(episode_number)
        with st.spinner('Fetching episode link...'):
            video_link = fetch_episode(episode_id)

        if video_link:
            # Display the video using Streamlit's video player
            st.video(video_link)

            # Buttons to open video in different players
            st.write("Open in your preferred media player:")

            if st.button('Open in IINA'):
                st.markdown(f'<a href="iina://{video_link}" target="_blank">Open in IINA</a>', unsafe_allow_html=True)

            if st.button('Open in PotPlayer'):
                st.markdown(f'<a href="potplayer://{video_link}" target="_blank">Open in PotPlayer</a>', unsafe_allow_html=True)

            if st.button('Open in VLC'):
                st.markdown(f'<a href="vlc://{video_link}" target="_blank">Open in VLC</a>', unsafe_allow_html=True)
        else:
            st.error("Episode not found or video link could not be retrieved. Please enter a valid episode number.")

if __name__ == "__main__":
    main()

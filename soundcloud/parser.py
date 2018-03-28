from bs4 import BeautifulSoup
from selenium import webdriver
from pprint import pprint


url = 'https://soundcloud.com/user774261744/sets/jamz'
driver = webdriver.PhantomJS()

# how to determine window size so that all tracks fit
# could also scroll to bottom
driver.set_window_size(2000, 2000)
driver.get(url)
page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')
tracklist = soup.find('div', attrs={'class': 'listenDetails__trackList'})

title_elements = tracklist.findall('a', attrs={'class': 'trackItem__trackTitle'})
username_elements = tracklist.findall('a', attrs={'class': 'trackItem__username sc-link-light'})

tracks_elements = dict(zip(title_elements, username_elements))
tracks = {title.text: username.text for title, username in track_elements.items()}

pprint(tracks)

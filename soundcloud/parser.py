from bs4 import BeautifulSoup


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    tracklist = soup.find('div', attrs={'class': 'listenDetails__trackList'})

    title_elements = tracklist.find_all('a', attrs={'class': 'trackItem__trackTitle'})
    username_elements = tracklist.find_all('a', attrs={'class': 'trackItem__username sc-link-light'})

    track_elements = dict(zip(title_elements, username_elements))
    tracks = {title.text: username.text for title, username in track_elements.items()}

    return tracks

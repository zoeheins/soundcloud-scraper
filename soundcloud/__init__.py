from .scraper import scrape
from .parser import SoundCloudParser


# TODO export tracks as .txt file

def get_playlist_tracks(playlist_url):
    html = scrape(playlist_url, 30000)
    return SoundCloudParser(html).parse_playlist()

def get_likes(username):
    url = 'https://soundcloud.com/{}/likes'.format(username)
    html = scrape(url, 1100000)
    return SoundCloudParser(html).parse_likes()

from .scraper import scrape
from .parser import parse

def get_tracks():
    html = scrape()
    return parse(html)

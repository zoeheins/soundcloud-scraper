from bs4 import BeautifulSoup


class SoundCloudParser():

    def __init__(self, html):
        self.soup = BeautifulSoup(html)

    def format_tracks(self, titles, usernames):
        tracks = dict(zip(titles, usernames))
        return {title.text: username.text for title, username in tracks.items()}

    def find_elements(self, element_type, class_name):
        return self.soup.find_all(element_type, attrs={'class': class_name})

    def parse_playlist(self):
        titles = self.find_elements('a', 'trackItem__trackTitle')
        usernames = self.find_elements('a', 'trackItem__username')
        return self.format_tracks(titles, usernames)

    def parse_likes(self):
        titles = [title.span for title in self.find_elements('a', 'soundTitle__title')]
        usernames = self.find_elements('span', 'soundTitle__usernameText')
        return self.format_tracks(titles, usernames)

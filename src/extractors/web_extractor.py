from bs4 import BeautifulSoup
import requests

class WebExtractor:
    def __init__(self, url):
        self.url = url
        self.html = None
        self.soup = None
        self.text = None

    def get_html(self):
        self.html = requests.get(self.url).text
        self.soup = BeautifulSoup(self.html, 'html.parser')

    def get_text(self):
        self.text = self.soup.get_text()
        return self.text

    def get_title(self):
        return self.soup.title.string

    def get_description(self):
        return self.soup.find('meta', attrs={'name': 'description'})['content']

    def get_keywords(self):
        return self.soup.find('meta', attrs={'name': 'keywords'})['content']

    def get_all(self):
        return {
            'title': self.get_title(),
            'description': self.get_description(),
            'keywords': self.get_keywords(),
            'text': self.get_text()
        }
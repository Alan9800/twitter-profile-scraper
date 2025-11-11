thonimport requests
from bs4 import BeautifulSoup

class TwitterParser:
    def __init__(self, url):
        self.url = url
        self.user_data = {}

    def scrape_profile(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')

        self.user_data['screen_name'] = self.get_user_name(soup)
        self.user_data['followers_count'] = self.get_followers_count(soup)
        self.user_data['bio'] = self.get_bio(soup)
        self.user_data['profile_image_url'] = self.get_profile_image_url(soup)
        return self.user_data

    def get_user_name(self, soup):
        name_tag = soup.find('h1', {'class': 'ProfileHeaderCard-name'})
        return name_tag.text.strip() if name_tag else None

    def get_followers_count(self, soup):
        followers_tag = soup.find('a', {'data-nav': 'followers'})
        return followers_tag.find('span').text.strip() if followers_tag else 0

    def get_bio(self, soup):
        bio_tag = soup.find('p', {'class': 'ProfileHeaderCard-bio'})
        return bio_tag.text.strip() if bio_tag else None

    def get_profile_image_url(self, soup):
        image_tag = soup.find('img', {'class': 'ProfileAvatar-image'})
        return image_tag['src'] if image_tag else None
import urllib.parse
import requests
from base64 import b64encode


API_PATH = '/artifactory/api/repositories'


def clean_url(url):
    parsed = urllib.parse.urlparse(url)
    parsed = parsed._replace(path='', scheme='')
    return urllib.parse.urlunparse(parsed).lstrip('//')


def basic_auth(username, password):
    token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'


class Repositories:
    def __init__(self, url, username, password):
        self.url = 'https://' + clean_url(url) + API_PATH
        self.headers = {"Authorization": basic_auth(username, password)}

    def get_url(self):
        return self.url

    def get_all(self):
        try:
            return requests.get(self.url, headers=self.headers)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def create_repo(self, repo_name, data):
        try:
            return requests.put(self.url + repo_name, json=data, headers=self.headers)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

import requests
from requests.auth import HTTPBasicAuth


def test_with_auth():
    response = requests.get("https://api.github.com/user", auth=HTTPBasicAuth("username", "pwd"))
    print(response.text)

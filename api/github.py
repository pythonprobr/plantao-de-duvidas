import requests


def get_avatar(user):

    resp = requests.get(f'https://api.github.com/users/{user}')
    return resp.json()['avatar_url']
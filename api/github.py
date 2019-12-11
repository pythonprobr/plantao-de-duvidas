import requests


def get_avatar(user):
    js = _get_js(user)
    # return js['avatar_url']

# Sendo usado para testes, veja em test_avatar.py
def _get_js(user):
    resp = requests.get(f'https://api.github.com/users/{user}')
    js = resp.json()
    return js
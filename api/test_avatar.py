from json import loads

import pytest
import responses

from api import github

_resp_renzon = loads('''{
"login": "renzon",
"id": 3457115,
"node_id": "MDQ6VXNlcjM0NTcxMTU=",
"avatar_url": "https://avatars3.githubusercontent.com/u/3457115?v=4",
"gravatar_id": "",
"url": "https://api.github.com/users/renzon",
"html_url": "https://github.com/renzon",
"followers_url": "https://api.github.com/users/renzon/followers",
"following_url": "https://api.github.com/users/renzon/following{/other_user}",
"gists_url": "https://api.github.com/users/renzon/gists{/gist_id}",
"starred_url": "https://api.github.com/users/renzon/starred{/owner}{/repo}",
"subscriptions_url": "https://api.github.com/users/renzon/subscriptions",
"organizations_url": "https://api.github.com/users/renzon/orgs",
"repos_url": "https://api.github.com/users/renzon/repos",
"events_url": "https://api.github.com/users/renzon/events{/privacy}",
"received_events_url": "https://api.github.com/users/renzon/received_events",
"type": "User",
"site_admin": false,
"name": "Renzo Nuccitelli",
"company": "Python Pro",
"blog": "https://www.python.pro.br",
"location": "Brazil",
"email": null,
"hireable": true,
"bio": null,
"public_repos": 156,
"public_gists": 56,
"followers": 453,
"following": 3,
"created_at": "2013-02-02T14:15:53Z",
"updated_at": "2019-12-03T20:43:44Z"
}''')


_resp_victor = loads('''{
"login": "renzon",
"id": 3457115,
"node_id": "MDQ6VXNlcjM0NTcxMTU=",
"avatar_url": "https://avatars2.githubusercontent.com/u/51089294?v=4",
"gravatar_id": "",
"url": "https://api.github.com/users/renzon",
"html_url": "https://github.com/renzon",
"followers_url": "https://api.github.com/users/renzon/followers",
"following_url": "https://api.github.com/users/renzon/following{/other_user}",
"gists_url": "https://api.github.com/users/renzon/gists{/gist_id}",
"starred_url": "https://api.github.com/users/renzon/starred{/owner}{/repo}",
"subscriptions_url": "https://api.github.com/users/renzon/subscriptions",
"organizations_url": "https://api.github.com/users/renzon/orgs",
"repos_url": "https://api.github.com/users/renzon/repos",
"events_url": "https://api.github.com/users/renzon/events{/privacy}",
"received_events_url": "https://api.github.com/users/renzon/received_events",
"type": "User",
"site_admin": false,
"name": "Renzo Nuccitelli",
"company": "Python Pro",
"blog": "https://www.python.pro.br",
"location": "Brazil",
"email": null,
"hireable": true,
"bio": null,
"public_repos": 156,
"public_gists": 56,
"followers": 453,
"following": 3,
"created_at": "2013-02-02T14:15:53Z",
"updated_at": "2019-12-03T20:43:44Z"
}''')


@pytest.fixture
def setup_responses():
    with responses.RequestsMock() as rsps:
        rsps.add(responses.GET, 'https://api.github.com/users/renzon',
                 json=_resp_renzon)
        yield rsps

def test_avatar(setup_responses):
    # Test
    assert "https://avatars3.githubusercontent.com/u/3457115?v=4" == github.get_avatar('renzon')


def test_js_called_with_user_name(setup_responses):
    # Test
    github.get_avatar('renzon')


@pytest.fixture
def setup_responses_victor():
    with responses.RequestsMock() as rsps:
        rsps.add(responses.GET, 'https://api.github.com/users/renzon',
                 json=_resp_renzon)
        rsps.add(responses.GET, 'https://api.github.com/users/Lnvictor',
                 json=_resp_victor)
        yield rsps


def test_avatar_victor(setup_responses_victor):
    # Test
    assert "https://avatars3.githubusercontent.com/u/3457115?v=4" == github.get_avatar('renzon')
    assert "https://avatars2.githubusercontent.com/u/51089294?v=4" == github.get_avatar('Lnvictor')

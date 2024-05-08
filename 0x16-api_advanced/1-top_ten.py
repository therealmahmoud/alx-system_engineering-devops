#!/usr/bin/python3
"""prints the titles of the first 10 hot posts
listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """
    prints the titles of the
    first 10 hot posts listed for a given subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {
        'User-Agent': 'linux:0x16.api.advanced:v1.0 (by ubuntu)'
    }
    params = {
        'limit': 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return
    data = response.json()['data']['children']
    for i in data:
        print(i['data']['title'])

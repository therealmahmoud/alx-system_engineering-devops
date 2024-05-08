#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """Returns a list of titles of all hot posts on a given subreddit."""
    global after
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {
        'User-Agent': 'linux:0x16.api.advanced:v1.0 (by ubuntu)'
    }
    params = {
        'after': after
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        next_ = response.json().get('data').get('after')
        if next_ is not None:
            after = next_
            recurse(subreddit, hot_list)
        data = response.json()['data']['children']
        for child in data:
            hot_list.append(child['data']['title'])
        return hot_list
    return None

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
        data1 = response.json().get('data').get('after')
        if data1 is not None:
            after = data1
            recurse(subreddit, hot_list)
        data = response.json()['data']['children']
        for i in data:
            hot_list.append(i['data']['title'])
        return hot_list
    return None

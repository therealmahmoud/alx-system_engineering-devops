#!/usr/bin/python3
""" Return the number of subs."""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers (not active users,
    total subscribers) for a given subreddit.
    """
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    headers = {
        'User-Agent': 'MyBot/0.1'
        }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json()
    subscribers = data['data']['subscribers']
    return subscribers

#!/usr/bin/python3
""" recursive function that queries the Reddit API"""
import requests
after = None
count_dic = []


def count_words(subreddit, word_list):
    """parses the title of all hot articles, and prints a sorted count of given
    keywords (case-insensitive, delimited by spaces) """
    global after
    global count_dic
    headers = {
        'User-Agent': 'linux:0x16.api.advanced:v1.0 (by ubuntu)'
    }
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

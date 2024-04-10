#!/usr/bin/python3

"""
this module contains a function that GET data from the Reddit Api
"""

import requests


def top_ten(subreddit):
    """
    GET and prints the first 10 hot posts listed for a given subreddit

    Args:
        subreddit (str): the name of subreddit

    """

    UA = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    URL = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    PARAMS = {'limit': 10}

    res = requests.get(URL, headers=UA, allow_redirects=False, params=PARAMS)

    if res.status_code != 200:
        print('None')
        return
    for post in res.json().get('data').get('children'):
        print(post.get('data').get('title'))

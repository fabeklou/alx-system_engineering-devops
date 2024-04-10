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

    UA = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    URL = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    PARAMS = {'limit': 10}

    res = requests.get(URL, headers=UA, allow_redirects=False, params=PARAMS)

    try:
        posts = res.json().get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))

    except Exception:
        print("None")

#!/usr/bin/python3

"""
this module contains a function that GET data from the Reddit Api
"""

import requests


def top_ten(subreddit):
    """
    GET and prints the first 10 hot posts listed for a given subreddit

    Args:
        subreddit (str): the name of the subreddit

    """

    if not subreddit or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    res = requests.get(url, headers=user_agent, params=params)
    dt = res.json()

    try:
        psts = dt.get('data').get('children')

        for pst in psts:
            print(pst.get('data').get('title'))

    except Exception:
        print("None")

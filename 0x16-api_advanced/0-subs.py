#!/usr/bin/python3

"""this module contains a function that GET data from the Reddit Api"""

import requests


def number_of_subscribers(subreddit):
    """
    GET and return the number of subscribers of the given subreddit

    Args:
        subreddit (str): the name of subreddit

    Returns:
        (int): the number of subscribers of the given subreddit
            or 0 if the subreddit does not exist
    """

    if not subreddit or not isinstance(subreddit, str):
        return 0

    UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    URL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    res = requests.get(URL, allow_redirects=False, headers=UA)

    try:
        return res.json().get('data').get('subscribers')
    except Exception:
        return 0

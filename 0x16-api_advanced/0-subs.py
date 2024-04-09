#!/usr/bin/python3

"""this module contains a function that GET data from the Reddit Api"""

import requests


def number_of_subscribers(sub):
    """GET and return the number of subscribers of the given subreddit

    Args:
        sub (str): the name of subreddit

    Returns:
        (int): the number of subscribers of the given subreddit
            or 0 if the subreddit does not exist
    """

    if not sub or not isinstance(sub, str):
        return 0

    UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    URL = 'https://www.reddit.com/r/{}/about.json'.format(sub)

    res = requests.get(URL, allow_redirects=False, headers=UA)

    if res.status_code != 200:
        return 0
    return res.json().get('data').get('subscribers')

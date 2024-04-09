#!/usr/bin/python3


def number_of_subscribers(sub):
    """GET and return the number of subscribers of the given subreddit

    Args:
        sub (str): the name of subreddit

    Returns:
        (int): the number of subscribers of the given subreddit
            or 0 if the subreddit does not exist
    """
    import requests

    URL = 'https://www.reddit.com/r/{}/about.json'.format(sub)

    res = requests.get(URL, allow_redirects=False)

    if res.status_code != 200:
        return 0
    return res.json().get('data').get('subscribers')

#!/usr/bin/python3

"""
this module contains a function that GET data from the Reddit Api
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively fetches hot articles from a subreddit and returns their titles

    Args:
        subreddit (str): The name of the subreddit
        hot_list (list): A list to accumulate the titles of hot articles.
        after (str): A token indicating the starting
            point for the next page of results.

    Returns:
        list or None: A list containing the titles of hot articles,
            or None if no results are found

    """

    UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    PARAMS = {'after': after}  if after else {}

    res = requests.get(URL, headers=UA, allow_redirects=False, params=PARAMS)

    if res.status_code != 200:
        return None

    data = res.json().get('data')
    if not data or 'children' not in data:
        return None

    for post in data.get('children'):
        hot_list.append(post.get('data').get('title'))

    # Check for pagination and recurse if there are more pages
    after = data.get('after', None)
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list

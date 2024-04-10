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

    params = {'show': 'all'}

    if subreddit is None or not isinstance(subreddit, str):
        return None

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}

    url = 'https://www.reddit.com/r/{}/hot/.json?after={}'.format(subreddit,
                                                                  after)

    response = requests.get(url, headers=user_agent, params=params)

    if (response.status_code != 200):
        return None

    all_data = response.json()

    try:
        raw1 = all_data.get('data').get('children')
        after = all_data.get('data').get('after')

        if after is None:
            return hot_list

        for i in raw1:
            hot_list.append(i.get('data').get('title'))

        return recurse(subreddit, hot_list, after)
    except:
        print("None")

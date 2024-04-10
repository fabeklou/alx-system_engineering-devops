#!/usr/bin/python3

"""
this module contains a function that GET data from the Reddit Api
"""

import requests


def count_words(subreddit, word_list=[], after=None, cleaned_dict=None):
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

    temp = []

    for i in word_list:
        temp.append(i.casefold())

    cleaned_word_list = list(dict.fromkeys(temp))

    if cleaned_dict is None:
        cleaned_dict = dict.fromkeys(cleaned_word_list)

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
    raw1 = all_data.get('data').get('children')
    after = all_data.get('data').get('after')

    if after is None:
        new = {k: v for k, v in cleaned_dict.items() if v is not None}

        for k in sorted(new.items(), key=lambda x: (-x[1], x[0])):
            print("{}: {}".format(k[0], k[1]))

        return None

    for i in raw1:
        title = i.get('data').get('title')

        split_title = title.split()

        split_title2 = [i.casefold() for i in split_title]

        for j in split_title2:
            if j in cleaned_dict and cleaned_dict[j] is None:
                cleaned_dict[j] = 1

            elif j in cleaned_dict and cleaned_dict[j] is not None:
                cleaned_dict[j] += 1

    count_words(subreddit, word_list, after, cleaned_dict)

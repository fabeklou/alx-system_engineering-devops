#!/usr/bin/python3

def number_of_subscribers(sub):
    import requests

    URL = 'https://www.reddit.com/r/{}/about.json'.format(sub)

    res = requests.get(URL, allow_redirects=False)

    if res.status_code != 200:
        return 0
    return res.json().get('data').get('subscribers')

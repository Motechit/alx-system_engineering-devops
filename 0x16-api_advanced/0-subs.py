#!/usr/bin/python3
"""function that queries the Reddit API
and returns the number of subscribers (not active 
users, total subscribers) for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API
    and returns the number of subscribers (not active 
    users, total subscribers) for a given subreddit"""
    
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "linux:0x16.api.advanced:v1.0.0 (by /u/Relevant-Repair-6162)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")

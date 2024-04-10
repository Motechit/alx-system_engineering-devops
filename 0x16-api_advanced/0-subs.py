#!/usr/bin/python3
"""function that queries the Reddit API
and returns the number of subscribers (not active 
users, total subscribers) for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API
    and returns the number of subscribers (not active 
    users, total subscribers) for a given subreddit"""
    
    apiUrl = "https://reddit.com/r/{}/about.json".format(subreddit)
    userAgent = "Mozilla/5.0"

    response = requests.get(apiUrl, headers={"user-agent": userAgent})
    if not response:
        return 0
    retValue = response.json().get('data').get('subscribers')
    if retValue:
        return retValue
    else:
        return 0

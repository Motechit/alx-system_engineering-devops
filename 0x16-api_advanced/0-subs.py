#!/usr/bin/python3
""" This function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """It return the total num of subscribers on a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")

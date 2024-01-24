#!/usr/bin/python3
"""
    This script uses reddit API to get the 10 hot posts
"""
import requests


def top_ten(subreddit):
    """Get 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'user-agent': '1-top_ten'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data").get("children")
    top_10_posts = "\n".join(post.get("data").get("title") for post in data)
    print(top_10_posts)

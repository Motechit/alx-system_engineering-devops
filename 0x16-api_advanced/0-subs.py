import requests

def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'user-agent': 'YourScript/1.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json().get("data")
            num_subs = data.get("subscribers")
            return num_subs
        else:
            # If the request was not successful, return 0 (invalid subreddit)
            return 0

    except Exception as e:
        # Handle exceptions (e.g., network issues, invalid URL)
        print(f"An error occurred: {e}")
        return 0

# Example usage:
subreddit_name = "python"
subscribers_count = number_of_subscribers(subreddit_name)
print(f"The subreddit '{subreddit_name}' has {subscribers_count} subscribers.")

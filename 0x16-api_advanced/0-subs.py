#!/usr/bin/python3
"""
Module that defines a function to query the Reddit API
for the number of subscribers in a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Python/requests:ALX-API-Advanced:v1.0 (by /u/yourusername)'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        print("Status Code:", response.status_code)  # Debug print
        print("Response Content:", response.text)    # Debug print
        if response.status_code == 200:
            data = response.json().get('data', {})
            return data.get('subscribers', 0)
        else:
            return 0
    except requests.RequestException:
        return 0

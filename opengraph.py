# pylint: disable=no-value-for-parameter
"""
Client of the Wagon OpenGraph API
"""

import requests

def fetch_metadata(url):
    """
    Returns the "data" dictionary of OpenGraph metadata found in HTML of given url
    """
    api_url = "https://opengraph.lewagon.com/"
    try:
        response = requests.get(api_url, params={'url': url})
        if response.status_code == 200:
            return response.json()
        else:
            return {}
    except requests.RequestException:
        return {}

# To manually test, please uncomment the following lines and run `python opengraph.py`:
# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(fetch_metadata("https://www.github.com"))

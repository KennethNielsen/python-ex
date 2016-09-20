"""Extract group results from EM 92"""

import requests
import codecs


def main():
    """Process wikpedia page"""
    # Get lines in html page
    request = requests.get('https://en.wikipedia.org/wiki/UEFA_Euro_1992')
    lines = request.text.split('\n')

    # ... here comes your solution


main()

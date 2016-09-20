"""Extract group results from EM 92"""

try:
    import requests
    print('Using requests')
except ImportError:
    requests = None
    print('Using saved file')

import codecs


def main():
    """Process wikpedia page"""
    # Get lines in html page
    if requests is not None:
        request = requests.get('https://en.wikipedia.org/wiki/UEFA_Euro_1992')
        html = request.text
    else:
        with codecs.open('EM92.html', encoding='utf-8') as file_:
            html = file_.read()
    lines = html.split('\n')

"""Extract group results from EM 92"""

import codecs

def main():
    """Process wikpedia page"""
    # Get lines in html page
    with codecs.open('EM92.html', encoding='utf-8') as file_:
        html = file_.read()
    lines = html.split('\n')

    # ... here comes your solution to the problem


main()

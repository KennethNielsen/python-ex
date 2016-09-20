"""Extract group results from EM 92"""

try:
    import requests
    print('Using requests')
except ImportError:
    requests = None
    print('Using saved file')

import codecs
from pprint import pprint

RESULTS = []
LAST_DATE = None

# This dict contain little bits of text that is unique to the line we
# are looking for. It is used in process_result_line
RESULT_LINE_IDENTIFIERS = {
    'align="right"': 'left_team',
    'align="center"': 'result',
    'white-space:nowrap"': 'right_team',
}


def extract_at_title(line):
    """Extract and information item at title"""
    title_index = line.index('title')
    start, end = [line.index(char, title_index) for char in '><']
    return line[start+1: end]


def process_result_line(line):
    """Process a results lines"""
    global LAST_DATE
    if '<td>' in line and line.count('<') == 2:
        LAST_DATE = line[4:-5]  # slicing strips the tags
    for identifier, info_type in RESULT_LINE_IDENTIFIERS.items():
        if identifier in line:
            info_item = extract_at_title(line)
            if info_type == 'left_team':
                RESULTS.append({info_type: info_item})
            else:
                RESULTS[-1][info_type] = info_item


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

    results_started = False
    table_start = 0
    for line in lines:
        # Look for the line that starts the results section
        if '<span class="mw-headline" id="Results">' in line:
            results_started = True

        # If we haven't found it yet, continue to the next line
        if not results_started:
            continue

        # If a table opens, increase the table counter
        if '<table' in line:
            table_start += 1

        # If we find a table close after 4 table starte we are done
        if '</table>' in line and table_start == 4:
            break

        # If we are in an equal numbered table, process the result line
        if table_start % 2 == 0:
            process_result_line(line)

main()
print(len(RESULTS))
pprint(RESULTS)

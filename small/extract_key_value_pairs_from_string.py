"""Exercise

The variable file_header contains metadata from the headers of a text
based data export file. The format of each line is:

name (type): value

From the header, extract the metadata and store it in a dictionary
using the name as the key AND type convert the value to python types e.g:

 {'Voltage': 1500.75}

NOTE how the value is of float type and not a strings and is extracted
file_header:


HINT: It might be useful for the solutions of this problem to also
make a dict that maps these foreign type names to python type
convertion functions e.g: {'string': str} and use that for the
convertion.

"""

file_header = """
Comment (string): This is the best experiment, like EVER
Date (string): 2016-04-01
Filename (string): ../../wishful_thinking/bummer/data.txt
Number of channels (integer): 4
Voltage (float): 1500.75
Pressure (float): 1.7E-10
""".strip()

metadata = {}

# ... your solution comes here

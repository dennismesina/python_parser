'''This tester will test the dm_parser.py'''

import dm_parser

my_parser = dm_parser.Parser("test.dm")

file_contents = my_parser.elements

print(file_contents)
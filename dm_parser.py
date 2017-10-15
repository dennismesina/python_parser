'''	Author: Dennis Mesina
	This parser will look for KV items and store them in a dictionary.
	Use this file for storing config or settings information at the top of files.
	The lines need to start with the '#' symbol and not be separated by an empty line
	
	Example:
	#	key 1 = value 1
	#	key 2 = value 2
	#	key 3 = list_of_items separated_by spaces

	...The rest of the file...

'''
import re

class Parser(object):
	elements = {}
	parser_list = []
	file_name = ""
	file = None

	def __init__(self, file_name):
		self.file_name = file_name
		self.main()

	#opens the file with file_name under "read only" mode
	def open_file(self):
		self.file = open(self.file_name, 'r')

	#closes the file
	def close_file(self):
		self.file.close()

	#get the lines at the top of the file before a newline separator, starting with #
	def get_usable_lines(self):
		usable_lines = []
		all_lines = self.file.readlines()
		for line in all_lines:
			if line[0] == '#':
				usable_lines.append(line)
			if line[0] == '\n':
				break
		self.parser_list = usable_lines

	#create a dictionary from the usable_lines and store it in elements{}
	def create_dictionary(self):
		for line in self.parser_list:
			key_value = re.search('#\s*(.*)?\s=\s(.*)?\n', line)
			if key_value:
				print(key_value.group(1), key_value.group(2))
				self.elements[key_value.group(1)] = key_value.group(2)

	#main will be run immidiately so that the elements are ready to be used.
	def main(self):
		self.open_file()
		self.get_usable_lines()
		self.create_dictionary()
		self.close_file()
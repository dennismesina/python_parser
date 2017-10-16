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
		state = ''
		for line in all_lines:
			if state == 'capture':
				usable_lines.append(line)
			elif line[0] == '[':
				state = 'capture'
				usable_lines.append(line)
		self.parser_list = usable_lines

	#create a dictionary from the usable_lines and store it in elements{}
	def create_dictionary(self):
		key = ''
		cmd_set = []
		for line in self.parser_list:
			key_cmdset = re.search('\[(.*?)\]', line)
			if key_cmdset:
				key = key_cmdset.group(1)
				cmd_set = []
			elif line[0] == '\n':
				self.elements[key] = cmd_set
			else:
				cmd_set.append(line)


	#main will be run immidiately so that the elements are ready to be used.
	def main(self):
		self.open_file()
		self.get_usable_lines()
		self.create_dictionary()
		self.close_file()
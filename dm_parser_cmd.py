'''	Author: Dennis Mesina
	This Parser will look for the command stanzas present in the config files.
	The commands in each stanza will be stored in a list to be executed later.
	Example:
	[ADD]
	SEND "Hello"
	RECEIVE "World"

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

	#get the lines after the first instance of a stanza (ex. [ADD])
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

	#create a list from the commands in the stanza and store it in elements{}
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
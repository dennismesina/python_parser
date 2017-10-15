'''This parser will look for KV items and store them in a dictionary'''
import re

class Parser(object):
	elements = {}
	parser_list = []
	file_name = ""
	file = None

	def __init__(self, file_name):
		self.file_name = file_name
		self.main()

	def open_file(self):
		self.file = open(self.file_name, 'r')

	def close_file(self):
		self.file.close()

	def get_usable_lines(self):
		usable_lines = []
		all_lines = self.file.readlines()
		for line in all_lines:
			if line[0] == '#':
				usable_lines.append(line)
		self.parser_list = usable_lines

	def create_dictionary(self):
		for line in self.parser_list:
			key_value = re.search('#\s*(.*)?\s=\s(.*)?\n', line)
			if key_value:
				print(key_value.group(1), key_value.group(2))
				self.elements[key_value.group(1)] = key_value.group(2)

	def main(self):
		self.open_file()
		self.get_usable_lines()
		self.create_dictionary()
		self.close_file()
'''This parser will look for KV items and store them in a dictionary'''
import re

class Parser(object):
	elements = {}
	parser_list = []
	file_name = ""
	file = None

	def __init__(self, file_name):
		self.file_name = file_name

	def open_file():
		self.file = open(self.file_name, 'r')

	def close_file():
		self.file.close()

	def get_usable_lines():
		usable_lines = []
		all_lines = self.file.readlines()
		for line in all_lines:
			if line[0] == '#':
				usable_lines.append(line)
		return usable_lines

	def create_dictionary(line_list):
		for line in line_list:
			key = re.search('#\s*(.*)?(?=\s=\s)', line)
			value = re.search('(?<=\s=\s)(.*)?\n', line)
			elements[key.group(1)] = value.group(0)

	def main():
		open_file()
		self.parser_list = get_usable_lines()
		create_dictionary(parser_list)
		close_file()
		return elements
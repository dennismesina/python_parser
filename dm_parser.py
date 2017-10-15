'''This parser will look for KV items and store them in a dictionary'''

class Parser(object):
	elements = {}
	file_name = ""

	def __init__(self, file_name):
		self.file_name = file_name

	
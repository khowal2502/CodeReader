from interfaces.file_reader import FileReader


class SingleFileReader(FileReader):

	def __init__(self, filename):
		self.file = open(filename, 'r')

	def get_file_lines(self):
		lines = self.file.readlines()
		return lines

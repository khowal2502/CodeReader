from classes.mediator import CodeParserMediator
from classes.single_file_reader import SingleFileReader


class CodeReaderService:

	blank_lines = None
	comment_lines = None
	code_lines = None

	code_parser = None
	file = None

	def __init__(self, language, file_name):
		self.code_lines = 0
		self.comment_lines = 0
		self.blank_lines = 0

		self.code_parser = CodeParserMediator(language).get_parser()
		self.file = SingleFileReader(file_name)

	def process_reading(self, lines):
		for line in lines:
			line_type = self.code_parser.parse_line(line)
			if line_type == "BLANK":
				self.blank_lines += 1
			elif line_type == "COMMENT":
				self.comment_lines += 1
			else:
				self.code_lines += 1

	def get_total_lines(self):
		return self.code_lines + self.comment_lines + self.blank_lines

	def process(self):
		lines = self.file.get_file_lines()
		self.process_reading(lines)


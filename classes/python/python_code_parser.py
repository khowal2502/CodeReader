from interfaces.code_parser import CodeParser
from classes.python import PythonBlankLineParser, PythonCommentParser


class PythonCodeParser(CodeParser):

	def __init__(self):
		self.blank_line_parser = PythonBlankLineParser()
		self.comment_line_parser = PythonCommentParser()

	def parse_line(self, line):

		if self.blank_line_parser.parse_line(line):
			return "BLANK"
		elif self.comment_line_parser.parse_line(line):
			return "COMMENT"
		else:
			return "CODE"

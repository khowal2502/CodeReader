from interfaces.code_parser import CodeParser
from classes.python import PythonBlankLineParser, PythonCommentParser
from classes.python.python_multi_line_comment_parser import PythonMultiLineCommentParser


class PythonCodeParser(CodeParser):

	def __init__(self):
		self.blank_line_parser = PythonBlankLineParser()
		self.comment_line_parser = PythonCommentParser()
		self.multi_line_parser = PythonMultiLineCommentParser()

	def parse_line(self, line):

		if self.blank_line_parser.parse_line(line):
			return "BLANK"
		elif self.comment_line_parser.parse_line(line):
			return "COMMENT"
		elif self.multi_line_parser.parse_line(line):
			return "MLC"
		else:
			return "CODE"

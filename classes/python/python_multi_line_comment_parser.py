from interfaces.line_parser import LineParser


class PythonMultiLineCommentParser(LineParser):

	def __init__(self):
		pass

	def parse_line(self, line):
		if line is None:
			return False

		line = line.replace(" ", "")
		if line[:3] == '"""':
			return True

		return False

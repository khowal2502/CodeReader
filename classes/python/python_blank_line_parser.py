from interfaces.line_parser import LineParser


class PythonBlankLineParser(LineParser):

	def __init__(self):
		pass

	def parse_line(self, line):
		if line == '\n' or line is None:
			return True

		if line.replace(" ", "") == "":
			return True

		return False

import sys

from classes.python.python_code_parser import PythonCodeParser


class CodeParserMediator:

	language_name = None

	def __init__(self, language_name):
		self.language_name = language_name

	def get_parser(self):
		if self.language_name == "Python":
			return PythonCodeParser()
		else:
			sys.exit("Language not supported")

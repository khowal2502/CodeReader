from bridge.code_reader_service import CodeReaderService


class CodeReader:
	def __init__(self):
		pass

	def process(self):
		print("Assuming file to be read: file_to_read")
		print("Assuming language to be: Python")

		service = CodeReaderService("Python", "file_to_read")
		print("Starting processing...")
		service.process()
		print("Processing Complete. Printing Data:")

		# Accessing variables directly for now. Can be made available
		# through getter methods if there are safety concerns
		print("Blank:", service.blank_lines)
		print("Comments:", service.comment_lines)
		print("Code:", service.code_lines)
		print("Total:", service.get_total_lines())


server = CodeReader()
server.process()

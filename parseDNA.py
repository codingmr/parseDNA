import sys

# TODO add argParser with options
# TODO add write to csv file

class parseDNA:
	def __init__(self, args):

		# Initializes an object with some default values
		## tries to ammend the default values to the arguments passed when script was run
		self.chunkSize = 5
		self.numberChunks = 3
		self.fileName = "data1.txt"
		self.args = args

		self.lst = []

		if len(args) > 2:
			try:
				self.chunkSize = int(args[1])
				self.numberChunks = int(args[2])
				self.fileName = args[3]
			except IndexError as error:
				print("Expected: chunkSize numberChunks fileName")

	def split_into_chunkgroups(self, chunkSize, numberChunks, indexPosition, data):
		# returns a tuple of the group of Chunks and the target
		j=0;
		return [ data[j:j+chunkSize] for j in range(indexPosition, chunkSize*numberChunks+indexPosition, chunkSize) ], data[j+chunkSize]

	def list_chunkgroups(self, chunkSize, numberChunks, data):
		# loops through each character calling split_into_chunksgroups
		# stays within the index bounds
		# returns a list of groups of Chunks and the target
		return [ self.split_into_chunkgroups(chunkSize, numberChunks, i, data) for i in range(len(data)-(chunkSize*numberChunks+2)) ]

	def formatPrintAll(self):
		print('\n'.join('{}: {}'.format(*k) for k in enumerate(self.lst)))

	def formatPrintOne(self, index):
		toString = ""

		for i in range(len(self.lst[1][0])):
			toString += "v" + str(i) + "=" + str(self.lst[1][0][i]) + " "
		toString += "with target == " + str(self.lst[1][1])

		print(toString)

	def parseFile(self):
		with open(self.fileName) as file:
			data = file.read()
			self.lst = self.list_chunkgroups(self.chunkSize, self.numberChunks, data)


dnaObj = parseDNA(sys.argv)
dnaObj.parseFile()
dnaObj.formatPrintAll()
dnaObj.formatPrintOne(108)

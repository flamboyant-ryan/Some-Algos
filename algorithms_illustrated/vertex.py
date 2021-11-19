
class Vertex():

	@classmethod
	def createVertex(cls, *labels):
		return [Vertex(name) for name in labels]

	def __init__(self, name):
		self.label = name

	def __hash__(self):
		return hash(self.label)

	def __eq__(self, other):
		return other.label == self.label

	def __str__(self):
		return f"<{self.label}>" 

	def __repr__(self):
		return f"{self.label}"

	def __lt__(self, other):
		return self.label <= other.label 

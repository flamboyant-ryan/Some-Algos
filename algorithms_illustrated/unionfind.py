class UnionFind():
	def __init__(self, objects):
		objects = set(objects)
		self.childToParent = {}
		self.heightofobjects = {}
		for obj in objects:
			self.childToParent[obj] = obj
			self.heightofobjects[obj] = 1

	def find(self, obj):

		child = obj
		parent = self.childToParent.get(child, None)
		if parent:
			while child != parent:
				child = parent
				parent = self.childToParent[child]

			return child
		raise Exception("object does not exist, sorry")


	def union(self, node1, node2):
		parent1, parent2 = self.find(node1), self.find(node2)
		heightNode1 = self.heightofobjects[parent1]
		heightNode2 = self.heightofobjects[parent2]

		if heightNode1 <= heightNode2:
			self.childToParent[parent1] = parent2
			self.heightofobjects[parent2] += 1
		else:
			self.childToParent[parent2] = parent1
			self.heightofobjects[parent1] += 1

if __name__ == "main":
	f = UnionFind([1,2,4,6,7,8,5,43])
	print(f.find(1))
	f.union(1, 2)
	print(f.find(1))
	f.union(1, 8)
	print(f.find(1))
	print(f.find(8))
	f.union(4, 5)
	f.union(4, 43)
	f.union(4, 7)
	f.union(7, 6)
	print(f.find(43))
	print(f.find(7))
	print(f.find(6))
	print(f.find(2))
	f.union(1, 4)
	print(f.find(2))



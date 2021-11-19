from collections import deque


class Tree():
	def __init__(self, val, leftchild=None, rightchild=None):
		self.val = val
		self.left = leftchild
		self.right = rightchild

	def printTree(self):
		nodes = deque([self])
		readnodes = []
		level = {self:0}

		while nodes:
			node = nodes.popleft()
			readnodes.append(node)
			if node.left:
				nodes.append(node.left)
				level[node.left] = level[node] + 1
			if node.right:
				nodes.append(node.right)
				level[node.right] = level[node] + 1

		currentlevel = 0
		for node in readnodes:
			if level[node] == currentlevel:
				print(node, "\t", end="")
			else:
				currentlevel = level[node]
				print()
				print(node, "\t", end="")

	def __str__(self):
		return f"{self.val}"

	def __repr__(self):
		return f"{self.val}"

if __name__ == "main":
	t = Tree(12)
	d = Tree(133, Tree(14, Tree(90)), Tree(1800))
	t.left = d
	t.right = Tree(89, Tree(1009, Tree(781), Tree(323)))
	t.printTree()
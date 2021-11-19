from tree import Tree

# alphabet of symbols for a binary code an optimal prefix code will be genereated for this
alphabet = {"A": 3, "B":2, "C":6, "D":8, "E":2, "F":6}


def createForest(alphabet):
	# creates single node trees of each symbols and appends them and thier frequency
	# values as a tuple  to a list 
	forest = []
	for symbol in alphabet:
		t = Tree(symbol)
		forest.append((t, alphabet[symbol]))
	return forest

def huffman(alphabet):
	forest = createForest(alphabet)
	while len(forest) >= 2:
		smallest = min(forest, key=lambda x: x[1])
		forest.remove(smallest)
		secondsmallest = min(forest, key=lambda x: x[1])
		forest.remove(secondsmallest)

		mergedtree = Tree(None, leftchild=smallest[0], rightchild=secondsmallest[0])
		combinedscore = smallest[1] + secondsmallest[1]

		forest.append((mergedtree, combinedscore))

	return forest[0]

def getOptimalPrefixfreeCode(alphabet, prefixfreecodeTree):
	pfc = {}
	def recursivefinding(path, tree):
		if not (tree.left and tree.right):
			return 	{tree.val: path}

		left, right = {}, {}
		if tree.left is not None:
			left = recursivefinding(path + '0', tree.left)
		if tree.right is not None:
			right = recursivefinding(path + '1', tree.right)
		
		left.update(right)
		return left

	pfc = recursivefinding('', prefixfreecodeTree)
	print(pfc)

d = createForest(alphabet)
print(d)
treeandscore = huffman(alphabet)

getOptimalPrefixfreeCode(alphabet, treeandscore[0])

class Heap():
	def __init__(self, arr=[]):
		self.indicies = {}
		self.heap = []
		if arr:
			self.__heapify(arr)

	def insert(self, obj):	
		self.heap.append(obj)
		length = len(self.heap)

		self.indicies[obj["obj"]] = length - 1

		while length // 2 >= 1:
			if self.heap[length - 1]["key"] < self.heap[(length // 2) - 1]["key"]:

				self.heap[length - 1], self.heap[(length // 2) - 1] = self.heap[(length // 2) - 1], self.heap[length - 1]

				self.indicies[self.heap[length - 1]["obj"]], self.indicies[self.heap[(length // 2) - 1]["obj"]] = self.indicies[self.heap[(length // 2) - 1]["obj"]], self.indicies[self.heap[length - 1]["obj"]]

				length = length // 2
			else:
				break

	def __heapify(self, arr):
		for obj in arr:
			self.insert(obj)

	def extractMin(self):
		if self.heap:
			result = self.heap[0]
			self.deleteItem(result["obj"])
			return result
		else:
			raise Exception("Heap empty")

	def deleteItem(self, object):

		index = self.indicies.pop(object, -1)
		if index == -1:
			raise Exception("object doesnt exist")

		if len(self.heap) == 1 or len(self.heap) == index + 1:
			self.heap.pop()
		else:

			self.heap[index] = self.heap[len(self.heap) - 1]
			self.heap.pop()
			self.indicies[self.heap[index]["obj"]] = index

			length = len(self.heap)
			node = index + 1

			while node <= length:
				if 2 * node > length:
					break
				elif 2 * node + 1 > length:
					minindex = 2 * node
				else:
					if self.heap[(2 * node) - 1]["key"] < self.heap[2 * node]["key"]:
						minindex = 2 * node
					else:
						minindex = 2 * node + 1

				if self.heap[node - 1]["key"] > self.heap[minindex - 1]["key"]:
					self.heap[node - 1], self.heap[minindex - 1] = self.heap[minindex - 1], self.heap[node - 1]
					self.indicies[self.heap[node - 1]["obj"]], self.indicies[self.heap[minindex - 1]["obj"]] = self.indicies[self.heap[minindex - 1]["obj"]], self.indicies[self.heap[node - 1]["obj"]]
					
					node = minindex
				else:
					break

	def contains(self, x):
		return x in [x['obj'] for x in self.heap]

	def __str__(self):
		return f"{[x['obj'] for x in self.heap]}"

# figs = [{"obj": int(i), "key":i} for i in range(100, 1, -1)]

# heap = Heap(figs)
# print(heap)
# heap.deleteItem(48)
# print(heap)
# while heap.heap:
# 	print(heap.extractMin())
# hay = [x[0] for x in sorted(heap.indicies.items(), key=lambda x : x[1])]
# print(hay == [x['obj'] for x in heap.heap])
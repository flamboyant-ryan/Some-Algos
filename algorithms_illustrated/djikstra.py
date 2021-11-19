from vertex import Vertex
from parsevertices import getGraph
from heap import Heap

s, v, d, o , j, f, h, k = Vertex.createVertex("s", "v", "d", "o", "j", "f", "h", "k")

G = {
	s: {v: 4, d: 7},
	v: {o: 5},
	d: {o: 1, j: 2},
	j: {o: 3},
	o: {},
	f: {h: 12},
	h: {f: 31},
	k: {h:33, f:9}
}

def straigthforwardStra(G, startvertex):
	# initialise alll the lengths to inffinity at first
	for v in G:
		if v != startvertex:
			v.explored = False
			v.length = float("inf")

	startvertex.length = 0
	processedVertices = set([startvertex])

	while True:
		smallestStraScore = float("inf")
		smallestStraEdge = None
		for v in G:
			if v in processedVertices:
				candidates = [w for w in G[v] if w not in processedVertices]
				for w in candidates:
					prospectivestrascore = v.length + G[v][w]
					if prospectivestrascore < smallestStraScore:
						smallestStraEdge = (v, w)
						smallestStraScore = prospectivestrascore

		if smallestStraEdge:
			v, w = smallestStraEdge
			processedVertices.add(w)
			w.length = smallestStraScore
		else:
			break

def heapStra(G, startvertex):
	processedVertices = set()
	unprocessedheap = Heap()

	startvertex.length = 0
	unprocessedheap.insert({"obj":startvertex, "key":startvertex.length})
	for v in G:
		if v != startvertex:
			v.length = float("inf")

			unprocessedheap.insert({"obj":v, "key":v.length})
	
	print(unprocessedheap)

	while unprocessedheap.heap:
		w = unprocessedheap.extractMin()
		print(unprocessedheap)
		processedVertices.add(w["obj"])
		w["obj"].length =  w["key"]
		w = w["obj"]
		for v in G[w]:
			try:
				unprocessedheap.deleteItem(v)
			except:
				break
			unprocessedheap.insert({"obj": v, "key":min(v.length, w.length + G[w][v])})



#heapStra(G,s)
straigthforwardStra(G, s)
for v in G:
	print(v, v.length)

G = getGraph("input_random_10_16.txt")
straigthforwardStra(G[0], G[1])
for v in G[0]:
	if int(v.label) in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]:
		print(v, v.length)
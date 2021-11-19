from vertex import Vertex
from random import randint
from heap import Heap


# heap based code doesnt duplicate cause i change the state of the vertex object
# actually i need to go back and refactor vertex cause it doesnt need that state

complexset = Vertex.createVertex("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m")
a, b, c, d, e, f, g, h, i, j, k, l, m = complexset

easyset = Vertex.createVertex("A", "B", "C", "D")
A, B, C, D = easyset

G_easy = {
	A: {B: 1, C: 4, D: 3},
	B: {A: 1, D: 2},
	C: {A: 4, D: 5},
	D: {A: 3, C: 5, B:2},
}

G_hard = {
	a: {b: 10},	
	b: {a: 10, c:2, d:4},	
	c: {b:2, d:3},	
	d: {c:3, b:4, e:12, g:4, h:14},	
	e: {f: 17, g:13, d:12},
	f: {e:17, g:9, i:6},	
	g: {e:13, d:4, f:9, i:3},	
	h: {d:14, l:21, i:8},	
	i: {j:11, f:6, g:3, h:8},
	j: {i:11, k:30},
	k: {j:30, m:9, l:14},
	l: {k:14, h:21},
	m: {k:9}

}

# Prim's Algortihms its a lot like djistkra but its a bit a different

def naivePrim(G, listofvertices):
	theotherside = {listofvertices[randint(0, len(listofvertices) - 1)]}
	t = []

	while True:
		frontierExtendingEdges = []
		cheapestfrontierExtendingEdge = None
		for v in G:
			if v in theotherside:
				candidates = [w for w in G[v] if w not in theotherside]
				candidates.sort(key=lambda w: G[v][w])
				
				if candidates:
					frontierExtendingEdge = (v, candidates[0])
					frontierExtendingEdges.append(frontierExtendingEdge)
		

		if frontierExtendingEdges:
			cheapestfrontierExtendingEdge = min(frontierExtendingEdges, 
														key= lambda edge : G[edge[0]][edge[1]])
			v, w = cheapestfrontierExtendingEdge
			t.append(cheapestfrontierExtendingEdge)
			theotherside.add(w)
		else:
			break

	return t


print("naive")	
print(naivePrim(G_easy, easyset))
print(naivePrim(G_hard, complexset))


# officially broken code, i changed back the vertex object, reimplement
def heapAssitedPrim(G, listofvertices):
	s = listofvertices[0]
	theotherside = {s}
	t = []
	heap = Heap() 
	
	winneredges = {}

	# initialisation
	for v in G:
		if v != s:
			if v in G[s]:
				v.cost = G[s][v]
				winneredges[v] = (s, v)
			else:
				winneredges[v] = None

			heap.insert({"obj":v, "key":v.cost})
	
	while heap.heap:
		w = heap.extractMin()["obj"]
		theotherside.add(w)
		t.append(winneredges[w])

		for u in G[w]:
			if  u not in theotherside and G[w][u] < u.cost:
				heap.deleteItem(u)
				u.cost = G[w][u]
				winneredges[u] = (w, u)
				heap.insert({"obj":u, "key":u.cost})


	print(t)
	return t	
print("heapbased")

def compareListOfTuples(tuples1, tuples2):
	def ignorePositionsHash(tup):
		return hash((tup[0], tup[1])) if tup[0] < tup[1] else hash((tup[1], tup[0]))

	if tuples1 and tuples2:
		listOfHashedtuples1 = sorted([ignorePositionsHash(tup) for tup in tuples1])
		listOfHashedtuples2 = sorted([ignorePositionsHash(tup) for tup in tuples2])

		for i, num in enumerate(listOfHashedtuples1):
			if num != listOfHashedtuples2[i]:
				return False
		return True
	return False

print(compareListOfTuples([(1,2)], [(1,2)]))
print(compareListOfTuples([(2,2)], [(2,1)]))
print(compareListOfTuples([(1,2), (34, 5)], [(1,2), (12,5)]))
print(compareListOfTuples([(10,21), (34, 5), (4,5)], [(34, 5), (21,10), (5, 4)]))
print(compareListOfTuples(
		heapAssitedPrim(G_easy, easyset), 
		naivePrim(G_easy, easyset)
		)
	)
print(compareListOfTuples(
	heapAssitedPrim(G_hard, complexset), 
	naivePrim(G_hard, complexset)
	)
)
from unionfind import UnionFind
from vertex import Vertex

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

def getEdges(G):
	def ignorePositionsHash(tup):
		return hash((tup[0], tup[1])) if tup[0] < tup[1] else hash((tup[1], tup[0]))

	edgehashes = set()
	edges = []
	for v in G:
		for w in G[v]:
			if ignorePositionsHash((v, w)) not in edgehashes:
				edges.append({"edge":(v, w), "weight":G[v][w]})
				edgehashes.add(ignorePositionsHash((v,w)))
	return edges

def kruskal(G):
	# iteraatively choose the cheapest edges that dont form a cycle
	# leading to a minimal forest that eventually merges into the mst

	U = UnionFind(G.keys())
	mst = []
	edges = getEdges(G)	
	edges.sort(key=lambda x : x["weight"])
	for edge in edges:
		v = edge["edge"][0]
		u = edge["edge"][1]
		if U.find(v) != U.find(u):
			mst.append(edge["edge"])
			U.union(v, u)
	return mst

print(kruskal(G_easy))
print(kruskal(G_hard))


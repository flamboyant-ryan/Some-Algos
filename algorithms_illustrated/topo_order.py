from vertex import Vertex

a, b, c, d, e= Vertex.createVertex("a", "b", "c", "d", "e")

G = {
	a: set([b, e]),
	b: set([d]),
	c: set(),
	d: set(),
	e: set([b, c]),
	
}

for v in G:
	print(v)
	v.explored = False

label = len(G)


def toposort(G):	
	for v in G:
		if not v.explored:
			dfs_topo(G, v)

def dfs_topo(G, v):
	global label
	v.explored = True
	for w in G[v]:
		if not w.explored:
			dfs_topo(G, w)

	v.label = label
	label -= 1 

toposort(G)

for v in G:
	print(v)
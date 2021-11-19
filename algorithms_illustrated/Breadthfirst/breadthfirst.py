from collections import deque
from vertex import Vertex

# create vertices
a, b, c, d, e, f = Vertex.createVertex("a", "b", "c", "d", "e", "f")

# initialize graph as an adjacency List
G = {
	a: [b],
	b: [c, a],
	c: [b, e, d, f],
	d: [c, e],
	e: [d, c],
	f: [e]
	
}

def breadthfirst(G, s):
	# initially mark all the vertices as unexplored with nan lenght
	for v in G:
		if v != s:
			v.explored = False
			v.length = float("inf")
	
	# mark the start vertex as explored and push into queue
	s.length = 0
	s.explored = True
	unprocessed = deque([s])
	# as long as we have unexplored vertices in the queue
	while unprocessed:
		v = unprocessed.popleft()
		for w in G[v]:
			if not w.explored:
				w.length = v.length + 1 
				w.explored = True
				unprocessed.append(w)

		print(v, "\t", "distance", v.length)

breadthfirst(G, a)

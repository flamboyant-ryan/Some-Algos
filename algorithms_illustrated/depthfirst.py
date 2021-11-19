
from vertex import Vertex

a, b, c, d, e, f, g, h, j, i, t, u, v, l= Vertex.createVertex("a", "b", "c", "d", "e", 
												"f", "g", "h", "j", "i", "t", "u", "v", "l")
G = {
	a: set([b]),
	b: set([c, h, a]),
	c: set([b, h, g, e, d]),
	d: set([c, e]),
	e: set([d, c]),
	g: set([c]),
	h: set([b, c]),
	j: set([l]),
	l: set([j, t, u]),
	t: set([l]),
	u: set([l, v]),
	v: set([u])
}

for v in G:
	v.explored = False

def depthfirst(G, s):
	for v in G[s]:
		if not v.explored:
			v.explored = True
			print(v)
			depthfirst(G, v)

depthfirst(G, a)
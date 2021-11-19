# solving the maximum independent set problem, for a path graph

import functools
from vertex import Vertex

complexset = Vertex.createVertex("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m")
a, b, c, d, e, f, g, h, i, j, k, l, m = complexset

easyset = Vertex.createVertex("A", "B", "C", "D")
A, B, C, D = easyset

G_easy = {
	A: 1,
	B: 4,
	C: 5,
	D: 4,
}
# @functools.lru_cache(maxsize=100)
def recursivemwis(vertices, weights):
	if len(vertices) == 0:
		return 0
	if len(vertices) == 1:
		return weights[vertices[0]]

	s1 = recursivemwis(vertices[:-1], weights)
	s2 = recursivemwis(vertices[:-2], weights)
	return max(s1, s2 + weights[vertices[-1]])


print(recursivemwis(list(G_easy.keys()), G_easy))

def itermwis(vertices, weights):
	subproblems = [0 for x in range(len(vertices) + 1)]
	subproblems[1] = weights[vertices[0]]

	for i in range(1, len(vertices)):
		subproblems[i + 1] = max(subproblems[i], subproblems[i - 1] + weights[vertices[i]])

	return subproblems
print(itermwis(list(G_easy.keys()), G_easy))




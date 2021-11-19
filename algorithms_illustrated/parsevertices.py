from vertex import Vertex

def fileLength(filename):
	lines = 0
	for line in open(filename):
		lines += 1
	return lines


def getGraph(filename):
	numberofverices = fileLength(filename)
	vertices = [Vertex(i + 1) for i in range(numberofverices)]
	G = {}


	with open(filename) as file:
		for line in file.readlines():
			line = line.split("\t")
		
			v = vertices[int(line[0]) - 1]
			l = line[-1].split(",")
		
			G[v] = {vertices[int(l[0]) - 1]: int(l[1][:-1])}
			for pair in line[1:-1]:
				pair = pair.split(",")
				G[v].update({vertices[int(pair[0]) - 1]: int(pair[1])})
			

	return (G, vertices[0])



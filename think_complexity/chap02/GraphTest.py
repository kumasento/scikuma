from chap02.Graph import Vertex, Graph, Edge

v1 = Vertex('v1')
v2 = Vertex('v2')
e1 = Edge(v1, v2)
g = Graph([v1, v2], [e1])

# test case - get_edge
assert g.get_edge(v1, v2) == e1
assert g.get_edge(v2, v1) == e1
assert g.get_edge(v1, v1) is None

# test case - remove_edge
v3 = Vertex('v3')  # add new vertex
g.add_vertex(v3)
e2 = Edge(v1, v3)  # add new edge based on v3
g.add_edge(e2)
assert g.get_edge(v1, v3) == e2
assert g.get_edge(v1, v3) != e1
g.remove_edge(e2)
assert g.get_edge(v1, v3) is None

# test case - vertices
assert type(g.vertices()).__name__ == 'list'
assert len(g.vertices()) == 3

# test case - edges
g.add_edge(e2)
e3 = Edge(v2, v3)
g.add_edge(e3)
assert type(g.edges()).__name__ == 'list'
assert len(g.edges()) == 3
assert e1 in g.edges()
assert e2 in g.edges()
assert e3 in g.edges()

# test case - out_vertices
vs = g.out_vertices(v1)
assert type(vs).__name__ == 'list'
assert len(vs) == 2
assert v2 in vs
assert v3 in vs
assert v1 not in vs
assert g.out_vertices(Vertex('v4')) is None

# test case - out_edges
es = g.out_edges(v1)
assert type(es).__name__ == 'list'
assert len(es) == 2
assert e1 in es
assert e2 in es
assert e3 not in es

g.remove_edge(e1)
g.remove_edge(e2)
g.remove_edge(e3)

assert len(g.edges()) == 0
g.add_all_edges()
assert len(g.edges()) == 3
# assert e1 not in g.edges()  # new edge

print 'All tests passed'

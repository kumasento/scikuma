# Code for a graph data structure


class Vertex(object):
    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__


class Edge(tuple):
    def __new__(cls, e1, e2):
        return tuple.__new__(cls, (e1, e2))

    def __repr__(self):
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__


class Graph(dict):
    def __init__(self, vs=[], es=[]):
        """
        Graph is inherited from dict, which means it can be "indexed".
        vs is an initial vertex array
        es is an initial edge array
        """
        for v in vs:
            self.add_vertex(v)
        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """
        v is a Vertex object
        """
        self[v] = {}  # initial edge set is empty

    def add_edge(self, e):
        """
        e is an Edge object, which is inherited from a tuple
        """
        v, w = e  # 2-tuple
        # Undirected
        self[v][w] = e
        self[w][v] = e

    # Exercise #2-2.3
    def get_edge(self, v, w):
        try:
            return self[v][w]
        except KeyError:
            return None

    # Exercise #2-2.4 - we assume each two nodes only have atmost 1 edge
    def remove_edge(self, e):
        v, w = e
        del self[v][w]
        del self[w][v]

    # Exercise #2-2.5 - get vertices from the graph
    def vertices(self):
        return self.keys()

    # Exercise #2-2.6 - get edges
    def edges(self):
        """
        iterate all the keys and return a set of edges
        :return: list of edges
        """
        edges = set()
        for v in self:
            for w in self[v]:
                edges.add(self[v][w])
        return list(edges)

    # Exercise #2-2.8 - get out vertices
    def out_vertices(self, v):
        """
        get out vertices for input vertex v
        :param v: Vertex
        :return: a list of vertices
        """
        try:
            return self[v].keys()
        except KeyError:
            return None

    # Exercise #2-2.9 - get out edges
    def out_edges(self, v):
        """
        get out edges from one input vertex
        :param v: vertex
        :return: a list of edges
        """
        try:
            return self[v].values()
        except KeyError:
            return None

    # Exercise #2-2.10 - add all edges
    def add_all_edges(self):
        """
        iterate all the vertices in the graph, and try to add edges between
        every two vertices.
        It will not override original edges
        :return: None
        """
        for v in self:
            for w in self:
                if v == w:
                    continue

                if w in self[v]:
                    # self[v][w] exists
                    if v in self[w]:
                        # self[w][v] exists
                        continue
                    else:
                        self[w][v] = self[v][w]
                else:
                    if v in self[w]:
                        # self[w][v] exists
                        self[v][w] = self[w][v]
                    else:
                        # both don't exists
                        self[v][w] = self[w][v] = Edge(v, w)
        return None

    # Exercise 2-3
    def add_regular_edges(self, degree):
        """
        add edges to make this graph regular
        :param degree: degree for each vertex
        :return:
        """
        if degree >= len(self.keys()) - 1:
            # degree can't be larger than max number of vertices minus 1
            return None

        return None

class Queue:
    '''
        Python list implementation of a FIFO Queue
    '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)


class Graph:
    '''
        >>> g1 = {'B': ['E', 'C'],
        ...       'F': [],
        ...       'C': ['F'],
        ...       'A': ['D', 'B'],
        ...       'D': ['C'],
        ...       'E': ['F']}
        >>> g = Graph(g1)
        >>> g.bfs('A')
        ['A', 'B', 'D', 'C', 'E', 'F']

        >>> g2 = {'Bran': ['East', 'Cap'],
        ...       'Flor': [],
        ...       'Cap':  ['Flor'],
        ...       'Apr':  ['Dec', 'Bran'],
        ...       'Dec':  ['Cap'],
        ...       'East': ['Flor']}
        >>> g = Graph(g2)
        >>> g.bfs('Apr')
        ['Apr', 'Bran', 'Dec', 'Cap', 'East', 'Flor']
    '''
    def __init__(self, graph_repr):
        self.adjacency_list = graph_repr

    def bfs(self, start):
        x=Queue()
        x.enqueue(start)
        visited=[]
        visited+=[start]
        while x.isEmpty()!=True:
            node=x.dequeue()
            for n in sorted(self.adjacency_list[node]):
                if n not in visited:
                    visited+=[n]
                    x.enqueue(n)
        return visited


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)